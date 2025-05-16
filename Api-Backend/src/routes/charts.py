from fastapi import APIRouter
from fastapi.responses import FileResponse
import matplotlib.pyplot as plt
import pickle
import os
from ..config import RESULT_DIR, HISTORY_PATH

router = APIRouter()

@router.get("/accuracy")
async def get_accuracy():
    plot_path = os.path.join(RESULT_DIR, "accuracy_plot.png")
    if not os.path.exists(plot_path):
        with open(HISTORY_PATH, "rb") as f:
            history = pickle.load(f)
        plt.figure(figsize=(8, 6))
        plt.plot(history["accuracy"], label="Train Accuracy", color="blue")
        plt.plot(history["val_accuracy"], label="Validation Accuracy", color="red")
        plt.title("Model Accuracy")
        plt.xlabel("Epochs")
        plt.ylabel("Accuracy")
        plt.legend()
        plt.grid(True)
        plt.savefig(plot_path)
        plt.close()
    return FileResponse(plot_path, media_type="image/png")

@router.get("/loss")
async def get_loss():
    plot_path = os.path.join(RESULT_DIR, "loss_plot.png")
    if not os.path.exists(plot_path):
        with open(HISTORY_PATH, "rb") as f:
            history = pickle.load(f)
        plt.figure(figsize=(8, 6))
        plt.plot(history["loss"], label="Train Loss", color="blue")
        plt.plot(history["val_loss"], label="Validation Loss", color="red")
        plt.title("Model Loss")
        plt.xlabel("Epochs")
        plt.ylabel("Loss")
        plt.legend()
        plt.grid(True)
        plt.savefig(plot_path)
        plt.close()
    return FileResponse(plot_path, media_type="image/png")