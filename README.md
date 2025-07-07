# Dyslexia Assistive Handwriting Recognition System ✍️🧠

This project is a real-time handwriting recognition system built to assist children with Dyslexia. It leverages a custom-trained Roboflow character recognition model to interpret hand-drawn alphabets from a React-based canvas and return accurate predictions via a FastAPI backend.

---

## 🔍 Features

- 🎨 Draw characters in real-time using a canvas interface
- 📦 Roboflow cloud-based model integration for A–Z classification
- 📡 FastAPI backend for handling predictions and file uploads
- 🔒 CORS-compliant and React-compatible API
- ⚡ Instant feedback with predicted character and confidence score
- 📐 Scalable architecture for future NLP grammar correction, sentence building, and learning loop (planned Phase 4)

---

## 🛠️ Tech Stack

| Component   | Tech Used                            |
|-------------|--------------------------------------|
| Frontend    | React, JavaScript, HTML5 Canvas      |
| Backend     | FastAPI, Python                      |
| Model       | Roboflow (YOLOv8 - A–Z classifier)   |
| Hosting     | Localhost (dev), Render/Vercel (prod)|
| Others      | CORS Middleware, Fetch API, Blob     |

---

## 🚀 Running Locally

### Backend (FastAPI)

uvicorn main:app --reload

### Frontend (React)

- npm install
- npm start
- 
- Make sure localhost:3000 (React) and localhost:8000 (FastAPI) are running.

