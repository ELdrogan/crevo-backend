
from fastapi import FastAPI, Request
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class ScriptRequest(BaseModel):
    prompt: str

@app.post("/generate-script")
async def generate_script(data: ScriptRequest):
    # Placeholder response, to be connected to OpenAI later
    return {"script": f"Generated script based on prompt: {data.prompt}"}

@app.get("/")
async def read_root():
    return {"message": "CreVo backend is running!"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
