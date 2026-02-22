# 🤟 SignLearn — Vietnamese Sign Language Learning Platform

A full-stack web application for learning and practicing Vietnamese Sign Language (VSL) with **real-time AI recognition** powered by YOLOv11.

---

## 🖥️ Demo

### Home Page
![Home Page](res/Screenshot%202026-02-22%20112353.png)

### Course Catalog
![Course Catalog](res/Screenshot%202026-02-22%20112408.png)

### Live AI Practice — Real-time Hand Sign Detection
> Detecting `xin_chao` with **70.9% confidence** via webcam feed.

![Practice Page](res/Screenshot%202026-02-22%20112638.png)

### Backend API (FastAPI + Swagger UI)
![Backend API](res/Screenshot%202026-02-22%20112713.png)

---

## 🚀 Tech Stack

| Layer | Technology |
|---|---|
| **Frontend** | Next.js 15, TypeScript, Tailwind CSS, Radix UI |
| **Backend** | FastAPI, Uvicorn, SQLAlchemy |
| **AI Model** | YOLOv11 (Ultralytics) — hand sign detection |
| **Auth** | JWT (python-jose), Argon2 password hashing |
| **Database** | SQLite (via SQLAlchemy ORM) |

---

## ✨ Features

- 📖 **Course Catalog** — Structured lessons from Beginner to Intermediate (Vietnamese Alphabet, Greetings, Basic Verbs, Common Nouns, and more)
- 🎥 **Real-time Practice** — Webcam-based hand sign recognition using YOLOv11; displays bounding boxes, confidence scores, and detection statistics
- 📊 **Progress Tracking** — Monitor learning achievements across sessions
- 🔐 **Authentication** — User registration, login, and admin login with JWT
- 🛠️ **Admin Monitoring** — `/admin/users` endpoint to list all users

---

## 🏗️ Project Structure

```
vsl_web_new/
├── backend/            # FastAPI backend
│   ├── main.py         # App entry point, CORS, DB setup
│   ├── auth/           # Register, Login, JWT utilities
│   ├── modules/        # Database connection, ORM models
│   ├── yolo/           # /yolo/predict endpoint + model loading
│   └── monitor/        # Admin monitoring routes
├── frontend/           # Next.js 15 frontend
│   ├── app/            # App Router pages (Home, Courses, Practice, Progress, Profile)
│   └── components/     # camera-feed.tsx — core webcam + detection component
├── model/              # YOLO model weights (.pt files)
├── res/                # Screenshots / demo assets
├── requirement.txt     # Python dependencies
└── .env                # Environment variables (DB_URL, JWT secret)
```

---

## ⚙️ Getting Started

### Prerequisites
- [Conda](https://docs.conda.io/) with an `envy` environment (Python 3.10+)
- [Node.js](https://nodejs.org/) 18+

### 1. Backend

```bash
# Activate the conda environment
conda activate envy

# Install Python dependencies
pip install -r requirement.txt

# Start the FastAPI server (from project root)
python -m uvicorn backend.main:app --host 127.0.0.1 --port 8000 --reload
```

Backend runs at: **http://127.0.0.1:8000**
API docs (Swagger): **http://127.0.0.1:8000/docs**

### 2. Frontend

```bash
cd frontend
npm install
npm run dev
```

Frontend runs at: **http://localhost:3000**

---

## 🔑 Environment Variables

Create a `.env` file in the project root:

```env
DB_URL=sqlite:///path/to/vsl_web_new/vsl.db
SECRET_KEY=your_secret_key_here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

## 🤖 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/auth/register` | Register a new user |
| `POST` | `/auth/login` | User login |
| `POST` | `/auth/admin/login` | Admin login |
| `POST` | `/auth/log` | Log an event |
| `POST` | `/yolo/predict` | Run hand sign inference on a base64 image |
| `GET` | `/admin/users` | List all users (admin only) |
| `GET` | `/health` | Health check |
