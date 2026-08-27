import asyncio
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from mcp_use import MCPAgent, MCPClient
from mcp.server.fastmcp import FastMCP
import os

# Initialize FastMCP server
mcp = FastMCP("client")

def setup_environment():
    """Setup environment variables and check for required API keys."""
    load_dotenv()
    
    # Check for required API keys
    groq_api_key = os.getenv("GROQ_API_KEY")
    if not groq_api_key:
        raise ValueError(
            "GROQ_API_KEY not found in environment variables. "
            "Please set it in your .env file or environment variables."
        )
    
    os.environ["GROQ_API_KEY"] = groq_api_key

async def run_memory_chat():
    """Run a chat using MCPAgent's built-in conversation memory."""
    try:
        # Setup environment and check API keys
        setup_environment()

        # Config file path - change this to your config file
        config_file = "server/weather.json"

        print("Initializing chat...")

        # Create MCP client and agent with memory enabled
        client = MCPClient.from_config_file(config_file)
        llm = ChatGroq(model="qwen-qwq-32b")

        # Create agent with memory_enabled=True
        agent = MCPAgent(
            llm=llm,
            client=client,
            max_steps=15,
            memory_enabled=True,  # Enable built-in conversation memory
        )

        print("\n===== Interactive MCP Chat =====")
        print("Type 'exit' or 'quit' to end the conversation")
        print("Type 'clear' to clear conversation history")
        print("==================================\n")

        try:
            # Main chat loop
            while True:
                # Get user input
                user_input = input("\nYou: ")

                # Check for exit command
                if user_input.lower() in ["exit", "quit"]:
                    print("Ending conversation...")
                    break

                # Check for clear history command
                if user_input.lower() == "clear":
                    agent.clear_conversation_history()
                    print("Conversation history cleared.")
                    continue

                # Get response from agent
                print("\nAssistant: ", end="", flush=True)

                try:
                    # Run the agent with the user input (memory handling is automatic)
                    response = await agent.run(user_input)
                    print(response)

                except Exception as e:
                    print(f"\nError: {e}")

        finally:
            # Clean up
            if client and client.sessions:
                await client.close_all_sessions()

    except ValueError as e:
        print(f"Configuration Error: {e}")
        print("\nPlease make sure you have:")
        print("1. Created a .env file in your project root")
        print("2. Added your GROQ_API_KEY to the .env file like this:")
        print("   GROQ_API_KEY=your_api_key_here")
        return

@mcp.tool()
async def chat_with_agent(message: str) -> str:
    """Chat with the MCP agent.
    
    Args:
        message: The message to send to the agent
    """
    try:
        # Setup environment and check API keys
        setup_environment()
        
        # Initialize the chat components
        config_file = "server/weather.json"
        client = MCPClient.from_config_file(config_file)
        llm = ChatGroq(model="qwen-qwq-32b")
        agent = MCPAgent(
            llm=llm,
            client=client,
            max_steps=15,
            memory_enabled=True,
        )
        
        try:
            response = await agent.run(message)
            return response
        finally:
            if client and client.sessions:
                await client.close_all_sessions()
                
    except ValueError as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    asyncio.run(run_memory_chat())
