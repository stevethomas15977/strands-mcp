from mcp.client.streamable_http import streamablehttp_client
from strands import Agent
from strands.tools.mcp.mcp_client import MCPClient
import json
from dotenv import load_dotenv

load_dotenv()

def create_streamable_http_transport():
   return streamablehttp_client("http://localhost:8000/mcp/")

streamable_http_mcp_client = MCPClient(create_streamable_http_transport)

def main():
    # Use the MCP server in a context manager
    with streamable_http_mcp_client:
        # Get the tools from the MCP server
        tools = streamable_http_mcp_client.list_tools_sync()

        # Create an agent with the MCP tools
        agent = Agent(tools=tools)

        response = agent("What is 125 plus 375?")

    print(json.dumps(response, indent=2, default=str))

if __name__ == "__main__":
    main()