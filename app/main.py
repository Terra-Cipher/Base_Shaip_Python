from fastapi import FastAPI, Body, HTTPException, status
from .services.math_operations import perform_addition

app = FastAPI(
    title="Shaip Base API",
    openapi_url=None,
    docs_url=None,
    redoc_url=None
)

@app.post("/shaip")
def add_numbers(payload: dict = Body(...)):
    try:
        a = payload["a"]
        b = payload["b"]
    except KeyError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Missing required payload key: {e.args[0]}"
        )
    
    result = perform_addition(a, b)
    
    return {
        "a": a,
        "b": b,
        "result": result
    }