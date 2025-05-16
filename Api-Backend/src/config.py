import os
from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Model paths
MODEL_PATH = os.path.join(BASE_DIR, "models", "Model.h5")
HISTORY_PATH = os.path.join(BASE_DIR, "models", "History.pkl")

# Static paths
UPLOAD_DIR = os.path.join(BASE_DIR, "static", "uploads")
RESULT_DIR = os.path.join(BASE_DIR, "static", "results")

# Create directories if not exist
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(RESULT_DIR, exist_ok=True)

# Model config
IMG_SIZE = (224, 224)
class_names = ['Audi', 'Ford_Ranger', 'Honda_City',
               'Hyundai Creta', 'Mahindra Scorpio', 'Mazda_3',
               'Mitsubishi_Xpander', 'Rolls Royce', 'Swift',
               'Tata Safari', 'Toyota Innova', 'Toyota_Camry',
               'VinFast_Fadil', 'BMW X6', 'Kia K2']
