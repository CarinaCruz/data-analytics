from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.ai import generate_sql, validate_sql
from app.db import execute_query

class QueryRequest(BaseModel):
    prompt: str
    max_rows: int = 100

app = FastAPI(title="SQL Assistant API")

@app.post("/query")
async def query(req: QueryRequest):
    sql, explanation = generate_sql(req.prompt)
    issues = validate_sql(sql)
    if issues:
        raise HTTPException(status_code=400, detail={"errors": issues, "sql": sql})
    try:
        rows, columns = execute_query(sql, limit=req.max_rows)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {"sql": sql, "columns": columns, "rows": rows, "explanation": explanation}
