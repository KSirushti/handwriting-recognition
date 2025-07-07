# ✍️ Real-Time Assistive Handwriting Recognition System

This project is an AI-powered handwriting recognition assistant designed to help users classify handwritten A–Z characters in real-time. It features a canvas-based UI for drawing, backend-powered prediction using the Roboflow API, and supports user corrections to continuously improve the model.

---

## 🧠 Features

- Real-time character recognition from canvas drawings (A–Z).
- Prediction using Roboflow API integrated via FastAPI backend.
- Manual correction support to submit corrected labels.
- Correction data logged automatically for continuous learning.
- Responsive and accessible UI built with React.
- Supports character segmentation for multi-letter inputs (via Roboflow).

---

## 🛠️ Tech Stack

- **Frontend:** React, HTML5 Canvas, CSS Modules
- **Backend:** FastAPI, Python
- **ML Integration:** Roboflow Hosted API
- **Image Processing:** Base64 Encoding
- **Data Storage:** Local CSV and folder-based logging

---

## 📦 Project Structure

.
├── frontend/
│ ├── components/
│ │ ├── CanvasBoard.js
│ │ └── PredictionDisplay.js
│ ├── pages/
│ │ └── Home.js
│ ├── App.js
│ └── styles/
│ ├── Home.css
│ └── CorrectionDisplay.css
├── backend/
│ ├── main.py
│ ├── utils/
│ │ └── save_correction.py
│ └── data/
│ └── corrections/
├── requirements.txt
└── README.md

yaml
Copy
Edit

---

## 🚀 How to Run

### 🖥️ Frontend (React)

1. Navigate to the frontend folder:
   ```bash
   cd frontend
Install dependencies:

bash
Copy
Edit
npm install
Start the development server:

bash
Copy
Edit
npm start
⚙️ Backend (FastAPI)
Navigate to the backend folder:

bash
Copy
Edit
cd backend
Create and activate a virtual environment:

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install required packages:

bash
Copy
Edit
pip install -r requirements.txt
Run the FastAPI server:

bash
Copy
Edit
uvicorn main:app --reload
The backend runs on http://localhost:8000 and exposes endpoints for character prediction and correction logging.

🔐 API Key Setup
This project uses a Roboflow Hosted Inference API for character detection and classification.

IMPORTANT: You must replace the placeholder API key with your own.

How to Set It:
In roboflowAPI.js (inside frontend/api/):

javascript
Copy
Edit
const API_KEY = "YOUR_ROBOFLOW_API_KEY";  // Replace with your own key
🖼️ Screenshots
<!-- Add your screenshots here --> <!-- ![Canvas and Prediction UI](./assets/ui-screenshot.png) -->
📊 Data Logging
Corrected samples are stored under:

php-template
Copy
Edit
backend/data/corrections/<CorrectLabel>/<filename>.png
A CSV log (corrections.csv) is maintained with the image path and corrected label, aiding retraining and model improvement.

🧠 Future Enhancements
NLP-based correction and disambiguation

Model retraining from correction data

Multi-character word recognition

User login and personalized training

🤝 Acknowledgements
Roboflow for hosted model APIs

FastAPI for a blazing-fast backend

React for frontend interactivity
