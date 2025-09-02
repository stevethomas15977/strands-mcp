from mcp import StdioServerParameters, stdio_client
from strands import Agent
from strands.models import BedrockModel
from strands.tools.mcp import MCPClient
from strands.agent.agent_result import AgentResult

import os, json
from dotenv import load_dotenv

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

def main():
    result = documentation()
    print(json.dumps(result.message, indent=2))

if __name__ == "__main__":
    main()