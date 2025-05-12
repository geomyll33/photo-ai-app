
# 📸 AI-Powered Photo Search App

This app helps you search and organize your photos using AI. It detects faces, estimates age, identifies if a person is alone, and allows search by face similarity or metadata.

## 🚀 Quick Start (with Docker Compose)

1. Clone the repo:
   ```
   git clone <your-repo-url>
   cd photo-ai-app
   ```

2. Run with Docker:
   ```
   docker-compose up --build
   ```

3. Access the app:
   - UI: http://localhost:8501
   - API: http://localhost:8000/docs

## 🧪 Features

- Upload & analyze photos with DeepFace
- PostgreSQL metadata storage
- Face similarity search
- Fully containerized

## 📂 Structure

- `app.py`: FastAPI backend
- `streamlit_app.py`: Streamlit frontend
- `Dockerfile`: Backend container
- `Dockerfile.streamlit`: UI container
- `requirements.txt`: Python deps
- `uploads/`: Photo storage
