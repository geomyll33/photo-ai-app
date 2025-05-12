# 📸 AI-Powered Photo Search App

This app helps you search and organize your photos using AI. It detects faces, estimates age, identifies if a person is alone, and allows search by face similarity or metadata.

## ✅ Features

- Upload photos and auto-analyze them using DeepFace
- Estimate age, detect group or solo presence
- Search photos by person, age range, or similarity
- View latest 10 Google Photos using API
- PostgreSQL backend
- Streamlit frontend
- Docker-based deployment

## 🚀 Quick Start

### 1. Clone and extract

```
git clone <your-repo-url>
cd photo-ai-app
```

### 2. Run

```
docker-compose up --build
```

### 3. Authenticate Google Photos (first time only)

```
python auth_google_photos.py
```

### 4. Make sure to include in your project root:

- `credentials.json` (downloaded from Google Cloud Console)
- `google_credentials.json` (auto-generated after authentication)

## 🐳 Docker Volume Mounts

Update your docker-compose.yml to include:

```yaml
volumes:
  - ./uploads:/app/uploads
  - ./credentials.json:/app/credentials.json
  - ./google_credentials.json:/app/google_credentials.json
```

## 🗂 Project Structure

- `app.py`: FastAPI backend
- `streamlit_app.py`: UI interface
- `auth_google_photos.py`: run once to link Google Photos
- `Dockerfile` and `Dockerfile.streamlit`
- `requirements.txt`
- `credentials.json`, `google_credentials.json` (manually added)
