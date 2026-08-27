import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import uvicorn

# Create a FastAPI app
app = FastAPI()

# Get the current directory for static files
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

# Mount static files
app.mount("/static", StaticFiles(directory=CURRENT_DIR), name="static")

# Serve index.html at the root
@app.get("/")
async def read_root():
    return FileResponse(os.path.join(CURRENT_DIR, "index.html"))

# Serve weather_client.html
@app.get("/weather_client.html")
async def read_weather_client():
    return FileResponse(os.path.join(CURRENT_DIR, "weather_client.html"))

# Run the server
if __name__ == "__main__":
    print("Running static file server on http://127.0.0.1:8000")
    uvicorn.run(app, host="127.0.0.1", port=8000) 