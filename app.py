from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import pandas as pd
import numpy as np
from ortools切割优化算法 import CuttingOptimizer

app = FastAPI()

class CuttingRequest(BaseModel):
    width: float
    height: float
    pieces: list[dict]

@app.post("/optimize-cutting/")
async def optimize_cutting(request: CuttingRequest):
    optimizer = CuttingOptimizer(request.width, request.height, request.pieces)
    optimized_plan = optimizer.optimize()
    return JSONResponse(content={"optimized_plan": optimized_plan})

@app.post("/upload-file/")
async def upload_file(file: UploadFile = File(...)):
    contents = await file.read()
    df = pd.read_csv(BytesIO(contents))
    return JSONResponse(content={"message": "File uploaded successfully", "file_content": df.to_dict()})
