from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from roboflow import Roboflow

app = FastAPI()

# Roboflow setup
rf = Roboflow(api_key="km1lBlePpnFiHGkxqpRq")
project = rf.workspace().project("dyslexia-handwriting-a-z-tkne4")
model = project.version(1).model  # classification model

# CORS config
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3001"],  # React app port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Classification prediction endpoint
@app.post("/segment-and-predict")
async def segment_and_predict(file: UploadFile = File(...)):
    contents = await file.read()

    # Save image
    with open("temp.png", "wb") as f:
        f.write(contents)

    # Predict (no confidence/overlap for classification)
    prediction = model.predict("temp.png").json()
    top_prediction = prediction["predictions"][0] if prediction["predictions"] else {}

    return {
        "predictions": [
            {
                "char": top_prediction.get("class", "Unknown"),
                "confidence": top_prediction.get("confidence", 0)
            }
        ]
    }
