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

### 🖥️ Frontend (React)

1. Navigate to the frontend folder:

   ```bash
   cd frontend

2. Install dependencies:

   ```bash
      npm install

3.Start the development server:
   
---

### Backend (FastAPI)
1. Navigate to the backend folder:

   ```bash
   cd backend



## 🔐 API Key Setup

This project uses a **Roboflow Hosted Inference API** for character detection and classification.

> **IMPORTANT:** You must replace the placeholder API key with your own.

### How to Set It:

In `frontend/api/roboflowAPI.js`, update the following:

```javascript
const API_KEY = "YOUR_ROBOFLOW_API_KEY";  // Replace with your own key

