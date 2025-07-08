# Real-Time Assistive Handwriting Recognition System

This project is an AI-powered handwriting recognition assistant designed to help users classify handwritten A–Z characters in real-time. It features a canvas-based UI for drawing, backend-powered prediction using the Roboflow API, and supports user corrections to continuously improve the model.

---

## Features

- Real-time character recognition from canvas drawings (A–Z).
- Prediction using Roboflow API integrated via FastAPI backend.
- Manual correction support to submit corrected labels.
- Correction data logged automatically for continuous learning.
- Responsive and accessible UI built with React.
- Supports character segmentation for multi-letter inputs (via Roboflow).

---

## Tech Stack

- **Frontend:** React, HTML5 Canvas, CSS Modules
- **Backend:** FastAPI, Python
- **ML Integration:** Roboflow Hosted API
- **Image Processing:** Base64 Encoding
- **Data Storage:** Local CSV and folder-based logging

---
## How to Run

### Frontend (React)

1. Navigate to the frontend folder:

   ```bash
   cd frontend

2. Install dependencies:

   ```bash
      npm install

3. Start Development server:

   ```bash
      npm start
---

### Backend (FastAPI)
1. Navigate to the backend folder:

   ```bash
   cd backend
2. Create and activate a virtual environment:

   ```bash
      python -m venv venv
      source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Start Development server:

   ```bash
   pip install -r requirements.txt

4. Run the FastAPI server:

   ```bash
      uvicorn main:app --reload
---

## 🔐 API Key Setup

This project uses a **Roboflow Hosted Inference API** for character detection and classification.

> **IMPORTANT:** You must replace the placeholder API key with your own.

### How to Set It:

In `frontend/api/roboflowAPI.js`, update the following:

      const API_KEY = "YOUR_ROBOFLOW_API_KEY";  // Replace with your own key   

---

## 🖼️ Screenshots

![img1](https://github.com/user-attachments/assets/a7e6de44-3d08-4aef-bc15-5fc7ce1b1419)

---

## Data Logging
Corrected samples are stored under:

   `backend/data/corrections/<CorrectLabel>/<filename>.png`

A corrections.csv log is also maintained, recording the image path and corrected label for fine-tuning and retraining purposes.

---
## Future Enhancements
- NLP-based correction and word disambiguation
- Model retraining from collected corrections
- Multi-character word recognition
- User login and personalized learning

---
## Acknowledgements
- Roboflow — Hosted Inference API
- FastAPI — Modern Python backend
- React — Interactive frontend UI
