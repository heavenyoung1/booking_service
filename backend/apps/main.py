import uvicorn
from fastapi import FastAPI
from auth_service.routes.router import router

main_app = FastAPI()
main_app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("app.app:app", host="0.0.0.0", log_level="info")
