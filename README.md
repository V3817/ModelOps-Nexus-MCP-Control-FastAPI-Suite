# MCP Crash Course

A Python-based project for learning and experimenting with MCP (Model Control Protocol) and related technologies.

## Project Overview

This project serves as a crash course for working with MCP and related technologies. It includes FastAPI integration, embedding capabilities, and LangChain integration with Groq.

## Why This Project?

### Key Benefits
1. **Simplified Model Management**
   - Streamlined interface for model deployment and control
   - Unified approach to handling different types of models
   - Reduced complexity in model operations

2. **Enhanced Performance**
   - Asynchronous processing for better throughput
   - Optimized embedding operations
   - Efficient resource utilization

3. **Developer-Friendly**
   - Clear API documentation
   - Intuitive CLI tools
   - Comprehensive error handling

4. **Scalability**
   - Modular architecture for easy expansion
   - Support for multiple model types
   - Flexible deployment options

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd mcpcrashcourse
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -e .
```

## Project Workflow

### Server Architecture
The project consists of two main server components:
- `server/`: Contains the main application server implementation
- `mcpserver/`: Houses the MCP-specific server functionality

### Key Components

1. **FastAPI Integration**
   - RESTful API endpoints for model interaction
   - Async support for high-performance operations
   - Built-in documentation and testing capabilities
   - Automatic request validation
   - Swagger/OpenAPI documentation

2. **Embedding System**
   - Utilizes FastEmbed for efficient text embeddings
   - Supports various embedding models
   - Enables semantic search and similarity matching
   - Batch processing capabilities
   - Memory-efficient operations

3. **LangChain Integration**
   - Integration with Groq for LLM operations
   - Chain-based processing of model inputs/outputs
   - Customizable pipeline configurations
   - Support for complex workflows
   - Easy integration with external services

4. **MCP Implementation**
   - Model Control Protocol implementation
   - CLI tools for model management
   - Configuration and deployment utilities
   - Health monitoring and logging
   - Automatic failover support

### Internal Workings

1. **Request Processing Flow**
   ```
   Client Request → FastAPI Router → Model Handler → MCP Controller → Model Execution → Response Formatter → Client
   ```

2. **Model Management**
   - Automatic model loading and unloading
   - Resource allocation optimization
   - Concurrent request handling
   - State management and persistence

3. **Error Handling**
   - Graceful degradation
   - Detailed error reporting
   - Automatic recovery mechanisms
   - Logging and monitoring

### Development Workflow

1. **Local Development**
   - Start the development server:
     ```bash
     python main.py
     ```
   - The server runs on `localhost:8000` by default
   - API documentation available at `/docs`
   - Hot-reloading for development
   - Debug mode support

2. **Model Integration**
   - Configure models in the appropriate server directory
   - Set up environment variables for API keys
   - Test model interactions through the API endpoints
   - Model versioning support
   - A/B testing capabilities

3. **Testing and Deployment**
   - Run automated tests
   - Deploy to production environment
   - Monitor model performance and API metrics
   - Continuous integration support
   - Automated deployment pipelines

### Common Operations

1. **Starting the Server**
   ```bash
   python main.py
   ```

2. **Accessing API Endpoints**
   - Use the FastAPI documentation interface
   - Make HTTP requests to the appropriate endpoints
   - Handle responses and errors appropriately
   - Rate limiting and throttling
   - Authentication and authorization

3. **Model Management**
   - Use MCP CLI tools for model operations
   - Configure model parameters
   - Monitor model performance
   - Model version control
   - Resource allocation management

## Project Structure

- `main.py`: Main entry point of the application
- `server/`: Server-related components
- `mcpserver/`: MCP server implementation
- `pyproject.toml`: Project configuration and dependencies
- `finalmcp.pdf`: Documentation or course materials

## Dependencies

The project uses several key dependencies:
- FastAPI (>=0.115.12)
- FastEmbed (>=0.6.1)
- LangChain-Groq (>=0.3.2)
- MCP-Use (>=1.2.8)
- MCP[CLI] (>=1.6.0)


