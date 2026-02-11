# Project Structure Overview

This repository contains a full-stack application for learning Vietnamese Sign Language (VSL) with real-time AI feedback. The application consists of a modern Next.js frontend, a FastAPI backend, and a legacy Streamlit prototype.

## 🏗️ High-Level Architecture

The system is composed of two main parts:

1.  **Frontend (Next.js)**: A modern web interface for users to browse courses, practice signs, and track progress.
    -   It captures video from the user's webcam.
    -   It sends frames to the backend for analysis.
    -   It displays real-time feedback and progress.
2.  **Backend (FastAPI)**: An API server that handles:
    -   **YOLO Object Detection**: Receives images from the frontend and runs inference using a YOLOv11 model to detect hand signs.
    -   **Authentication**: User registration and login (JWT).
    -   **Database**: Stores user data, progress, and monitoring metrics (using SQLAlchemy).

## 📂 Directory Structure Map

```
.
├── Home.py                 # (Legacy) Main entry point for the Streamlit prototype app.
├── README.md               # Basic project instructions.
├── structure.txt           # Credentials file (admin credentials).
├── requirement.txt         # Python dependencies for the backend and Streamlit app.
├── run/                    # Scripts for running/testing models.
│   └── test.py             # Streamlit app for testing YOLO model with webcam.
├── test/                   # Standalone testing scripts.
│   └── test.py             # Python script for testing YOLO with OpenCV window.
│
├── model/                  # Contains the YOLO model weights.
│   ├── v9_l_yolo11.pt      # Large YOLOv11 model.
│   └── v9_n_yolo11.pt      # Nano YOLOv11 model (faster, less accurate).
│
├── backend/                # The main API server (FastAPI).
│   ├── main.py             # Application entry point. Sets up routes, CORS, and DB.
│   ├── auth/               # Authentication module.
│   │   ├── routes.py       # Login/Register endpoints.
│   │   ├── models.py       # User database models.
│   │   └── utils.py        # Hashing and token utilities.
│   ├── modules/            # Core backend modules.
│   │   ├── database.py     # Database connection (SQLAlchemy) and session management.
│   │   └── yolo_db.py      # Database models for storing YOLO detections/logs.
│   ├── monitor/            # System monitoring module.
│   │   └── routes.py       # Endpoints for system health/metrics.
│   └── yolo/               # YOLO Model integration.
│       ├── routes.py       # The `/predict` endpoint. Handles image inference.
│       └── model/          # Directory where the model file is loaded from.
│
└── frontend/               # The main web application (Next.js).
    ├── app/                # Next.js App Router source code.
    │   ├── page.tsx        # Landing page (Home).
    │   ├── layout.tsx      # Main layout wrapper.
    │   ├── practice/       # Practice page logic.
    │   │   └── page.tsx    # The practice interface connecting to webcam & backend.
    │   ├── courses/        # Course listing pages.
    │   ├── auth/           # Login/Register pages.
    │   └── ... (admin, profile, progress, etc.)
    ├── components/         # Reusable React components.
    │   ├── camera-feed.tsx # KEY COMPONENT: Captures video, sends to backend, draws boxes.
    │   └── ... (ui, charts, navbar, etc.)
    ├── pages/              # (Legacy/Mixed) Contains Streamlit Python pages (Course.py, Practice.py, etc.).
    │                       # These seem to belong to the `Home.py` Streamlit app, not Next.js.
    └── public/             # Static assets (images, icons).
```

## 🔍 Key Components Breakdown

### 1. Backend (`backend/`)

*   **`main.py`**: Initializes the FastAPI app, connects to the database, and includes routers from `auth`, `yolo`, and `monitor`. It also configures CORS to allow the frontend to communicate with it.
*   **`yolo/routes.py`**: This is the core of the AI functionality.
    *   It loads the YOLO model (`v9_n_yolo11.pt`).
    *   It exposes a `POST /yolo/predict` endpoint.
    *   It accepts a base64-encoded image, decodes it, runs inference, and returns bounding box coordinates and class labels.
*   **`modules/database.py`**: Handles database connections using SQLAlchemy. It expects a `DB_URL` environment variable.

### 2. Frontend (`frontend/`)

*   **Technology**: Next.js 15 (App Router), Tailwind CSS, TypeScript.
*   **`app/practice/page.tsx`**: The main interactive page. It uses the `CameraFeed` component.
*   **`components/camera-feed.tsx`**:
    *   Accesses the user's webcam.
    *   Captures frames and sends them to `http://127.0.0.1:8000/yolo/predict`.
    *   Receives detection data and draws bounding boxes on a canvas overlaying the video.
    *   Calculates accuracy and updates the UI.

### 3. Legacy / Prototype (`Home.py` & `frontend/pages/*.py`)

*   The root `Home.py` and the Python files inside `frontend/pages/` (e.g., `Course.py`, `Practice.py`) form a separate Streamlit application.
*   This appears to be an earlier version or a quick prototype of the application, as it duplicates functionality found in the Next.js app (courses, practice, etc.).
*   **Note**: The Next.js app (`frontend/app`) does *not* use these Python files.

## ⚠️ Important Notes for Developers

1.  **Hardcoded Paths**:
    *   `backend/yolo/routes.py` contains a hardcoded absolute path to the model file: `D:\WORK\Python\web\github_zone\vsl_web_new\backend\yolo\model\v9_n_yolo11.pt`. This will cause errors when running on a different machine. You should update this to use a relative path or an environment variable.
    *   `backend/modules/database.py` contains a hardcoded path to the `.env` file.

2.  **Environment Variables**:
    *   The backend requires a `.env` file with `DB_URL` and potentially other secrets (e.g., for JWT).

3.  **Running the Project**:
    *   **Backend**: `uvicorn backend.main:app --reload` (Run from the root directory).
    *   **Frontend**: `npm run dev` (Run from `frontend/` directory).
