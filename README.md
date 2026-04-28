# 🧠 OncoScan AI: Brain & Breast Tumor Detection

OncoScan AI is an end-to-end medical imaging AI system designed to detect tumors in brain MRI and breast scans using deep learning. The system provides real-time predictions along with Grad-CAM visualizations for model interpretability.

This project demonstrates a production-grade MLOps pipeline using FastAPI, Docker, Kubernetes, and GitHub Actions.

🚀 Key Features<br>
🔍 Multi-Class Tumor Detection using CNN models<br>
🧠 Explainable AI (XAI) via Grad-CAM heatmaps<br>
⚡ FastAPI Backend for real-time inference<br>
🐳 Dockerized Deployment for portability<br>
☸️ Kubernetes (GKE) for scalable deployment<br>
🔄 CI/CD with GitHub Actions (build → test → deploy)<br><br>

## 🏗️ Project Architecture

- **Frontend**: Web UI for uploading scans and viewing inference results/GradCAM heatmaps.
- **Backend (FastAPI)**: Asynchronous Python REST API handling model inference and visualization.
- **AI Core (TensorFlow)**: Custom CNN implementations dynamically loaded for inference.
- **Containerization (Docker)**: Standardized application packaging.
- **Orchestration (Kubernetes)**: Deployment manifests for Google Kubernetes Engine (GKE).
- **CI/CD**: GitHub Actions

## 📂 Folder Structure

```
├── backend/                  # FastAPI Application Core
│   ├── models/               # Model lazy loaders
│   ├── utils/                # Inference, GradCAM, and Logging utilities
│   ├── config.py             # Global configurations
│   └── main.py               # API Endpoints (/predict, /gradcam)
├── frontend/                 # Web Application UI
├── documentation/            # Project documentation and artifacts
├── experiments/              # Model training experiments 
├── Dockerfile                # Image definition for the mlops-app
├── kubernetes-deployment.yaml# Kubernetes Deployment & LoadBalancer Service
├── .github/workflows/ci.yml  # CI/CD pipeline/GitHub Actions pipeline
├── run.py                    # Application Entrypoint
├── requirements.txt          # Python deployment dependencies
└── setup.py                  # Package installation logic
```

## 🚀 Getting Started

### Prerequisites

- Python 3.11+
- Docker
- Google Cloud SDK (for GKE deployments)
- `kubectl`

⚙️ Local Setup<br>
1️⃣ Clone the repo<br>
git clone https://github.com/<your-username>/Tumor_detection.git<br>
cd Tumor_detection<br><br>
2️⃣ Create virtual environment<br>
python -m venv venv<br>
venv\Scripts\activate   # Windows<br><br>
3️⃣ Install dependencies<br>
pip install -r requirements.txt<br>
pip install -e .<br><br>
4️⃣ Run the app<br>
python run.py<br><br>

👉 App runs at: http://127.0.0.1:8000<br>

### Containerized Execution (Docker)

1. **Build the image**:
   ```bash
   docker build -t mlops-app:latest .
   ```
2. **Run the container**:
   ```bash
   docker run -p 8000:8000 mlops-app:latest
   ```

☸️ Kubernetes Deployment (GKE)
kubectl apply -f kubernetes-deployment.yaml
kubectl get pods
kubectl get svc mlops-service
🔄 CI/CD Pipeline (GitHub Actions)

Pipeline defined in:

.github/workflows/ci.yml<br>

Workflow includes:<br>
✅ Code checkout<br>
✅ Dependency installation<br>
✅ Docker build & push<br>
✅ Deployment trigger<br>

🧪 Tech Stack<br>
Backend: FastAPI<br>
ML/DL: TensorFlow, CNN<br>
Explainability: Grad-CAM<br>
Containerization: Docker<br>
Orchestration: Kubernetes (GKE)<br>
CI/CD: GitHub Actions<br>
<br>
📸 Sample Output<br>
Tumor classification results<br>
GradCAM heatmaps highlighting regions of interest<br>
<br>
📌 Future Improvements<br>
🔄 Model drift monitoring<br>
📊 Bias analysis (age, demographics)<br>
⚡ Real-time streaming inference<br>
🔐 Authentication & access control<br>
<br>

## 🔬 Key Features

- **Multi-Class Detection**: Classifies scans to detect tumors effectively.
- **GradCAM Visualization**: Generates heatmaps to explain AI decision-making (Explainable AI).
- **Production-Ready**: Hosted via Uvicorn, packaged as a Docker container, and deployed seamlessly over Kubernetes.
- **Scalable Architecture**: Decoupled AI microservice design for easy feature expansions.


⭐ If you like this project

Give it a ⭐ on GitHub and feel free to fork!