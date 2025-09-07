from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/healthz")
def read_health_check():
    return {"status": "ok"}


if __name__ == "__main___":
    import uvicorn

    uvicorn.run(app, host= "0.0.0.0, port=8000")