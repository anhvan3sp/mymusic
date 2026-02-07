from fastapi import FastAPI

app = FastAPI(title="MyMusic API")

@app.get("/")
def root():
    return {"status": "ok", "message": "MyMusic API running"}
