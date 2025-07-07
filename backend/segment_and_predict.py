# backend/segment_and_predict.py

from fastapi import APIRouter, UploadFile, File
import requests

router = APIRouter()

ROBOFLOW_API = "https://detect.roboflow.com/dyslexia-handwriting-a-z-tkne4/1"
API_KEY = "km1lBlePpnFiHGkxqpRq"

@router.post("/segment-and-predict")
async def segment_and_predict(file: UploadFile = File(...)):
    image_bytes = await file.read()

    response = requests.post(
        f"{ROBOFLOW_API}?api_key={API_KEY}",
        files={"file": ("image.png", image_bytes, "image/png")},
    )

    if response.status_code != 200:
        return {"error": "Roboflow request failed"}

    detections = response.json()

    # Return just characters sorted by x
    boxes = detections.get("predictions", [])
    sorted_boxes = sorted(boxes, key=lambda x: x["x"])
    characters = [{"prediction": b["class"], "box": [b["x"], b["y"], b["width"], b["height"]]} for b in sorted_boxes]

    return {"characters": characters}
