from fastmcp.client.transports import StdioTransport
from fastmcp.client import Client
from mcp.server.fastmcp.exceptions import ToolError
import asyncio


async def run_client():
    # 1. Define the transport with the command to run the server
    transport = StdioTransport(
        command="python", args=["main.py"]  # Path to your FastMCP server script
    )

    # 2. Initialize the client with the transport
    client = Client(transport)

    # 3. Connect and interact
    async with client:
        try:
            result = await client.call_tool("greet", {"name": 'Dave', "formal": True})
            print("Tool succeeded:", result.data)

            result = await client.call_tool("greet", {"name": "Dave"})
            print("Tool succeeded:", result.data)

            result = await client.call_tool("add_numbers", {"a": 3.5, "b": 1.5})
            print("Tool succeeded:", result.content)

            result = await client.call_tool("word_stats", {"text": "hello world hello"})
            print("Tool succeeded:", result.content)

            result = await client.call_tool(
                "safe_divide", {"numerator": 10, "denominator": 2}
            )
            print("Tool succeeded:", result.data)

            result = await client.call_tool(
                "safe_divide", {"numerator": 10, "denominator": 0}, raise_on_error=False
            )
            print("Tool succeeded:", result.is_error)

        except ToolError as e:
            print(f"Tool failed: {e}")


if __name__ == "__main__":
    asyncio.run(run_client())
