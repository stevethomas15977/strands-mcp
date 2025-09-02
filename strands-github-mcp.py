from mcp.client.streamable_http import streamablehttp_client
from strands import Agent
from strands.tools.mcp.mcp_client import MCPClient
import json
from dotenv import load_dotenv
import os

load_dotenv()

def create_streamable_http_transport():
   return streamablehttp_client(url="https://api.githubcopilot.com/mcp/",
                                headers={"Authorization": f"Bearer {os.getenv('GITHUB_PAT')}"})

streamable_http_mcp_client = MCPClient(create_streamable_http_transport)

def main():
    # Use the MCP server in a context manager
    with streamable_http_mcp_client:
        # Get the tools from the MCP server
        tools = streamable_http_mcp_client.list_tools_sync()

        # Create an agent with the MCP tools
        agent = Agent(tools=tools)

        task = f"""
        For repo "stevethomas15977/public_afe":
        1) Call github.dependabot.list_alerts to list OPEN alerts (severity >= low).
        2) Summarize counts by severity and ecosystem.
        Ask me to confirm before write calls.
        """
        response = agent(task)

    print(json.dumps(response, indent=2, default=str))

if __name__ == "__main__":
    main()