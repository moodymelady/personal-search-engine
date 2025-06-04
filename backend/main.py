# backend/main.py

from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from search import search_exa

app = FastAPI()

@app.get("/search")
def search(query: str = Query(..., min_length=1)):
    results = search_exa(query, domains=["https://www.tiktok.com"])

    if not results:
        return JSONResponse({"message": "No results found"}, status_code=204)

    return {"results": results}

