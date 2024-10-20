from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World!"}

app.include_router(authenticated-route)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, log_level="info")

