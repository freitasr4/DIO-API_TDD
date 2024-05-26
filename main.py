from fastapi import FastAPI
from app.controllers.product_controller import router as product_router

app = FastAPI()

app.include_router(product_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
