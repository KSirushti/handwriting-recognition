from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse
from inference_sdk import InferenceHTTPClient
from PIL import Image
from uuid import uuid4
import io, os, base64
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = InferenceHTTPClient(
    api_url="https://serverless.roboflow.com",
    api_key="km1lBlePpnFiHGkxqpRq"  # Replace this
)


CORRECTION_DIR = "data/corrections"

class CorrectionRequest(BaseModel):
    image: str
    label: str
@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        image = Image.open(io.BytesIO(contents)).convert("RGB")

        temp_path = f"temp_{uuid4().hex[:8]}.jpg"
        image.save(temp_path)

        try:
            result = client.run_workflow(
                workspace_name="siru",
                workflow_id="active-learning",
                images={"image": temp_path},
                use_cache=True
            )
        except Exception as e:
            os.remove(temp_path)
            return JSONResponse(content={"error": f"Roboflow Error: {str(e)}"}, status_code=500)

        os.remove(temp_path)

        try:
            prediction_data = result['results'][0]['predictions'][0]
            return {
                "prediction": prediction_data['class'],
                "confidence": round(prediction_data['confidence'], 4)
            }
        except (KeyError, IndexError):
            return JSONResponse(content={"error": "No predictions returned by Roboflow."}, status_code=500)

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)


@app.post("/corrections")
async def save_correction(data: CorrectionRequest):
    try:
        label = data.label.upper()
        folder_path = os.path.join(CORRECTION_DIR, label)
        os.makedirs(folder_path, exist_ok=True)

        image_data = base64.b64decode(data.image.split(",")[1])
        filename = f"{label}_{uuid4().hex[:8]}.png"
        file_path = os.path.join(folder_path, filename)

        with open(file_path, "wb") as f:
            f.write(image_data)

        return {"message": "Correction saved", "path": file_path}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
