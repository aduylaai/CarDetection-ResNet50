from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from .routes.predict import router as predict_router
from .routes.charts import router as charts_router
from .config import BASE_DIR

app = FastAPI(title="Car Detection API")

# Mount static files
app.mount("/static", StaticFiles(directory=f"{BASE_DIR}/static"), name="static")

# Include routers
app.include_router(predict_router, prefix="/api")
app.include_router(charts_router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "Car Detection API is running"}

