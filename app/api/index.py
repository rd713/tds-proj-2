from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import JSONResponse
import uvicorn

app = FastAPI()

@app.post("/api/")
async def solve(question: str = Form(...), file: UploadFile = File(None)):
    # Replace with actual logic, for now return test answer
    return JSONResponse({"answer": "This is a test response"})
