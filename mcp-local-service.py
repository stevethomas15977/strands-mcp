from mcp.server import FastMCP

mcp = FastMCP("Calculator Server")

@mcp.tool(description="Add two numbers together")
def add(x: int, y: int) -> int:
    """Add two numbers and return the result."""
    return x + y

def main():
    mcp.run(transport="streamable-http")

if __name__ == "__main__":
    main()





