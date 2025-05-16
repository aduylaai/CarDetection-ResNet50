import numpy as np
from PIL import Image
import tensorflow as tf
from keras._tf_keras.keras.applications.resnet50 import preprocess_input
from ..config import IMG_SIZE

def load_model(model_path):
    return tf.keras.models.load_model(model_path)

def preprocess_image(image_file, target_size=IMG_SIZE):
    img = Image.open(image_file).resize(target_size)
    img_array = np.array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)
    return img_array

def predict_image(model, processed_img, class_names):
    predictions = model.predict(processed_img, verbose=0)
    predicted_class_idx = np.argmax(predictions)
    confidence = float(100 * np.max(predictions))
    return class_names[predicted_class_idx], confidence