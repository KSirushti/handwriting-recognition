# main.py
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse
from PIL import Image
from pydantic import BaseModel
from fastapi import HTTPException
import io
import os
import base64
from uuid import uuid4

app = FastAPI()

# Enable CORS for React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    if not file:
        return JSONResponse(content={"error": "No file received"}, status_code=400)

    try:
        contents = await file.read()
        image = Image.open(io.BytesIO(contents)).convert("RGB")

        # TODO: Replace with your real Roboflow or model logic
        print("Image received for prediction.")
        return {"prediction": "S", "confidence": 0.98}

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

CORRECTION_DIR = "data/corrections"

class CorrectionRequest(BaseModel):
    image: str
    label: str

@app.post("/corrections")
def save_correction(data: CorrectionRequest):
    try:
        label = data.label.upper()
        folder_path = os.path.join(CORRECTION_DIR, label)
        os.makedirs(folder_path, exist_ok=True)

        image_data = base64.b64decode(data.image.split(",")[1])
        filename = f"{label}_{uuid4().hex[:8]}.png"
        with open(os.path.join(folder_path, filename), "wb") as f:
            f.write(image_data)

        return {"message": "Correction saved", "path": f"{folder_path}/{filename}"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))