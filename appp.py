from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from io import BytesIO
import pandas as pd
import numpy as np

# Certifique-se de que o módulo esteja no mesmo diretório ou instalado no seu ambiente
from ortools_corte_otimizacao import CuttingOptimizer  

app = FastAPI()

class CuttingRequest(BaseModel):
    width: float
    height: float
    pieces: list[dict]

@app.post("/optimize-cutting/")
async def optimize_cutting(request: CuttingRequest):
    try:
        # Instancia o otimizador com os dados fornecidos
        optimizer = CuttingOptimizer(request.width, request.height, request.pieces)
        optimized_plan = optimizer.optimize()
        return JSONResponse(content={"optimized_plan": optimized_plan})
    except Exception as e:
        # Retorna um erro genérico em caso de falha na otimização
        return JSONResponse(content={"error": str(e)}, status_code=500)

@app.post("/upload-file/")
async def upload_file(file: UploadFile = File(...)):
    try:
        # Lê o conteúdo do arquivo
        contents = await file.read()
        df = pd.read_csv(BytesIO(contents), encoding='utf-8')

        # Retorna o conteúdo do arquivo em formato JSON
        return JSONResponse(content={
            "message": "Arquivo enviado com sucesso",
            "file_content": df.to_dict(orient="records")
        })
    except Exception as e:
        # Retorna um erro se ocorrer algum problema na leitura do arquivo
        return JSONResponse(content={"error": str(e)}, status_code=500)
