🩺 Sleep Apnea Detection System

A smart and interactive web-based dashboard to detect and monitor Sleep Apnea using physiological data such as Heart Rate (HR) and SpO₂ levels.
Built using Python Flask and deployed using Render and Railway (alternative).

📑 Table of Contents

1. 🚀 Features
2. 🛠️ Tech Stack
3. 📊 Model Info
4. 🧪 Installation
5. 🌐 Deployment Guide
6. 📌 Project Status

1. 🚀 Features

👤 Admin and Patient Login/Register system
📤 Upload and analyze CSV data (Heart Rate & SpO₂)
📈 Real-time interactive graphs using Chart.js
🧠 Naive Bayes ML model for apnea prediction
📊 Role-based Dashboards (Admin & Patient)
🖨️ Printable Patient Reports
📱 Smartwatch data integration (Planned in Phase II)
☁️ Cloud health record storage (Planned in Phase II)

2. 🛠️ Tech Stack

Frontend: HTML5, CSS3, Bootstrap 5, Chart.js
Backend: Python, Flask, Flask-SQLAlchemy
Database: SQLite
ML Model: Naive Bayes Classifier
Deployment: Render, Railway

3. 📊 Model Info

Algorithm: Naive Bayes
Accuracy: 75.96%
Input Features: Heart Rate (bpm), SpO₂ (%)
Training Notebook: `train_model.ipynb`

4. 🧪 Installation

Step 1: Clone the repository

git clone https://github.com/yourusername/Final_sleep_apnea_project.git
cd Final_sleep_apnea_project

Step 2: Create virtual environment

python -m venv venv
source venv/bin/activate     # For Linux/macOS  
venv\Scripts\activate        # For Windows

Step 3: Install dependencies

pip install -r requirements.txt

Step 4: Run the application

python app.py
 
Then open: `http://127.0.0.1:5000` in your browser.

5. 🌐 Deployment Guide

Render Deployment (Free Cloud Hosting)

1. Push your code to GitHub

2. Create a `render.yaml` file in the root directory:

services:
  - type: web
    name: sleep-apnea-detector
    env: python
    buildCommand: "pip install -r requirements.txt"
    startCommand: "python app.py"
    plan: free
    autoDeploy: true

3. Go to [https://render.com](https://render.com)
   Click “New Web Service”
   Connect your GitHub repository
   It auto-detects render.yaml and deploys your app

Alternative: You can also deploy on [Railway](https://railway.app) by linking the GitHub repo and choosing Python as the runtime.

6. 📌 Project Status

Currently in Development

Phase I:
✔️ Functional Admin/Patient login
✔️ ML-based apnea prediction using HR & SpO₂
✔️ Dashboard with real-time visualizations
✔️ CSV upload and printable patient report

Phase II (Planned):
📱 Smartwatch integration for real-time vitals
☁️ Cloud-based patient health records
🧾 Enhanced reporting with health summaries & alerts


