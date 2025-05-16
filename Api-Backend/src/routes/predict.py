from fastapi import APIRouter, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
import os
from ..config import UPLOAD_DIR, CLASS_NAMES
from ..utils.utils import preprocess_image, predict_image
import tensorflow as tf
import shutil

router = APIRouter()

# Load model globally
model = tf.keras.models.load_model(os.path.join(os.path.dirname(__file__), "../../models/Model.h5"))

@router.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        # Validate file type
        if not file.content_type.startswith("image/"):
            raise HTTPException(status_code=400, detail="File must be an image")

        # Save uploaded file
        file_path = os.path.join(UPLOAD_DIR, file.filename)
        with open(file_path, "wb") as f:
            shutil.copyfileobj(file.file, f)

        # Preprocess and predict
        processed_img = preprocess_image(file_path)
        predicted_class, confidence = predict_image(model, processed_img, CLASS_NAMES)

        # Convert confidence to Python float
        confidence = float(round(confidence, 2))

        # Return result with file path for frontend
        return JSONResponse(content={
            "filename": file.filename,
            "predicted_class": predicted_class,
            "confidence": round(confidence, 2),
            "image_url": f"/static/uploads/{file.filename}"
        })

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))