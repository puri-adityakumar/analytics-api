from fastapi import FastAPI


from api.events import router as event_router

app = FastAPI()
app.include_router(event_router, prefix='/api/events')

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/healthz")
def read_health_check():
    return {"status": "ok"}


# if __name__ == "__main__":
#     import uvicorn

#     uvicorn.run(app, host= "0.0.0.0, port=8000")