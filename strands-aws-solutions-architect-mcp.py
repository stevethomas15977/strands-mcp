from mcp import StdioServerParameters, stdio_client
from strands import Agent
from strands.models import BedrockModel
from strands.tools.mcp import MCPClient
from strands.agent.agent_result import AgentResult
from IPython.display import Image, display
import os, json
from dotenv import load_dotenv
import shutil

load_dotenv()

aws_docs_client = MCPClient(
    lambda: stdio_client(
        StdioServerParameters(
            command="uvx", 
            args=["awslabs.aws-documentation-mcp-server@latest"]
        )
    )
)

aws_diag_client = MCPClient(
    lambda: stdio_client(
        StdioServerParameters(
            command="uvx", 
            args=["awslabs.aws-diagram-mcp-server@latest"]
        )
    )
)

SYSTEM_PROMPT = """
You are an expert AWS Certified Solutions Architect. Your role is to help customers understand best practices on building on AWS. 
You can query the AWS Documentation and generate diagrams. When you generate a diagram, 
you MUST tell the customer the full file path of the diagram in the format "The diagram is saved at: <filepath>".
"""

def documentation() -> AgentResult:
    with aws_docs_client:
        all_tools = aws_docs_client.list_tools_sync()
        agent = Agent(tools=all_tools, system_prompt=SYSTEM_PROMPT)

        query = "Get the documentation for AWS Lambda then find out the maximum timeout for Lambda function"

        # The agent() call returns an AgentResult object directly
        agent_result = agent(query)

        return agent_result

def diagram() -> AgentResult:

    diagram_dir = "./generated-diagrams"
    if not os.path.exists(diagram_dir):
        os.makedirs(diagram_dir)

    with aws_diag_client:
        all_tools = aws_diag_client.list_tools_sync()
        bedrock_model = BedrockModel(
            model_id="anthropic.claude-3-haiku-20240307-v1:0",
            temperature=0.7,
        )
        agent = Agent(tools=all_tools, 
                      model=bedrock_model,
                      system_prompt=SYSTEM_PROMPT)

        query = "Create a diagram of a website that uses AWS Lambda for a static website hosted on S3"
        print(f"Sending query to agent: {query}\n")

        # The agent() call returns an AgentResult object directly
        agent_result = agent(query)
        final_agent_response_text = agent_result

        final_agent_response_text = ""
        if hasattr(agent_result, 'response') and isinstance(agent_result.response, str):
            final_agent_response_text = agent_result.response
        elif hasattr(agent_result, 'content') and isinstance(agent_result.content, str):
            final_agent_response_text = agent_result.content
        elif hasattr(agent_result, 'output') and isinstance(agent_result.output, str): # Common for agent outputs
            final_agent_response_text = agent_result.output
        elif isinstance(agent_result, str): # If somehow it's just a string
            final_agent_response_text = agent_result
        else:
            # If none of the above, try converting to string as a last resort,
            # or you might need to access a specific field if it's a more complex object/dict
            try:
                final_agent_response_text = str(agent_result)
                print("DEBUG: Converted agent_result to string.")
            except Exception as e:
                print(f"ERROR: Could not extract text from AgentResult. Error: {e}")
                print("Please inspect the 'DEBUG: Attributes of agent_result' output above to determine the correct attribute for the response text.")


        print("\n--- Agent's Full Response Text ---")
        print(final_agent_response_text)
        print("--- End of Agent's Full Response Text ---\n")

        diagram_path = None
        if final_agent_response_text:
            path_marker = "The diagram is saved at: "
            if path_marker in final_agent_response_text:
                start_index = final_agent_response_text.find(path_marker) + len(path_marker)
                end_index = final_agent_response_text.find("\n", start_index)
                if end_index == -1:
                    end_index = len(final_agent_response_text)
                diagram_path_raw = final_agent_response_text[start_index:end_index].strip()
                diagram_path = diagram_path_raw.strip("`'\"")

                print(f"\nExtracted diagram path: '{diagram_path}'")
                if diagram_path and os.path.exists(diagram_path):
                    print(f"Creating diagram from: {diagram_path}")
                    # Save a copy to generated-diagrams if not already there

                    dest_path = os.path.join(diagram_dir, os.path.basename(diagram_path))
                    if os.path.abspath(diagram_path) != os.path.abspath(dest_path):
                        shutil.copy2(diagram_path, dest_path)
                        print(f"Diagram also saved to: {dest_path}")
                elif diagram_path:
                    print(f"Diagram file not found at the specified path: {diagram_path}")
                    print(f"Please ensure the path is correct and the diagram generation tool is saving to this location relative to your script's CWD or an absolute path.")
                    print(f"Current working directory: {os.getcwd()}")
                    expected_dir = os.path.dirname(diagram_path)
                    if os.path.exists(expected_dir):
                        print(f"Directory '{expected_dir}' exists.")
                        print(f"Files in '{expected_dir}': {os.listdir(expected_dir)}")
                    else:
                        print(f"Directory '{expected_dir}' does NOT exist.")
                else:
                    print("Could not find a valid diagram path string after extraction.")
            else:
                print("Agent did not provide a diagram path in the expected format in its response.")
        else:
            print("No textual response extracted from the agent's result.")

        return agent_result

def main():
    # result = documentation()
    result = diagram()

if __name__ == "__main__":
    main()