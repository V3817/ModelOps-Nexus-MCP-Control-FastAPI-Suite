import asyncio
import nest_asyncio
import os
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

# Apply nest_asyncio to allow nested event loops
nest_asyncio.apply()

async def main():
    # Get the current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    server_path = os.path.join(current_dir, "server.py")
    
    # Define server parameters
    server_params = StdioServerParameters(
        command="python",  # The command to run your server
        args=[server_path],  # Use the absolute path to the server
    )

    print(f"Connecting to server at: {server_path}")
    
    try:
        # Connect to the server
        async with stdio_client(server_params) as (read_stream, write_stream):
            async with ClientSession(read_stream, write_stream) as session:
                # Initialize the connection
                await session.initialize()
                print("Connected to server successfully!")

                # List available tools
                tools_result = await session.list_tools()
                print("Available tools:")
                for tool in tools_result.tools:
                    print(f"  - {tool.name}: {tool.description}")

                # Call our Weather Tool
                print("\nFetching weather alerts for California...")
                result = await session.call_tool("get_alerts", arguments={"state":"CA"})
                print(f"The weather alerts are = {result.content[0].text}")
    except Exception as e:
        print(f"Error: {e}")
        print("\nTroubleshooting tips:")
        print("1. Make sure the server is running in another terminal with: uv run mcpserver/server.py")
        print("2. Check that the server path is correct")
        print("3. Ensure you have all required dependencies installed")


if __name__ == "__main__":
    # Use nest_asyncio to handle the event loop
    asyncio.run(main())