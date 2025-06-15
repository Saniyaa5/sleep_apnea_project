🩺 Sleep Apnea Detection System

A smart and interactive web-based dashboard to detect and monitor sleep apnea using physiological data such as heart rate and SpO₂ levels. Built using Python Flask and deployed on Render.

📌 Table of Contents

1. [Features] 
2. [Project Structure] 
3. [Tech Stack] 
4. [Model Info] 
5. [Installation] 
6. [Render Deployment] 
7. [Status]


1. 🚀 Features

 👤 Admin and Patient login/register system
 📤 Upload and analyze CSV data (HR & SpO₂)
 📈 Real-time graph generation using Chart.js
 🧠 Naive Bayes ML model for apnea prediction
 📊 Interactive dashboards with zoom & pan
 🖨️ Printable patient reports
 📱 Smartwatch data integration (Phase-II)
 ☁️ Cloud health record storage (Phase-II)

2. 📁 Project Structure

Final_sleep_apnea_project/
├── app.py                       # Main Flask application
├── models.py                    # SQLAlchemy database models
├── train_model.ipynb            # Jupyter notebook for ML training
├── sleep_apnea.db               # SQLite database
├── naive_bayes_apnea_model.pkl  # Trained Naive Bayes model
├── naive_bayes_scaler.pkl       # Scaler for input features
├── render.yaml                  # Configuration for Render deployment
├── requirements.txt             # Python dependencies
├── README.md                    # Project documentation
├── uploads/                     # Uploaded CSV files
├── static/
│   ├── images/                  # Backgrounds and logos
│   └── *.png                    # Generated graphs
└── templates/
    ├── base.html                # Base layout
    ├── index.html               # Home page
    ├── login.html               # Login page
    ├── register.html            # User registration
    ├── forgot.html              # Password reset
    ├── admin_dashboard.html     # Admin's dashboard
    ├── patient_dashboard.html   # Patient's dashboard
    └── report.html              # Report generation page

3. 🛠️ Tech Stack

    Frontend: HTML5, CSS3, Bootstrap 5, Chart.js
    Backend: Python, Flask, SQLAlchemy
    Database: SQLite
    ML Model: Naive Bayes Classifier
    Deployment:  Render

4. 📊 Model Info

Algorithm: Naive Bayes
Accuracy: 75.96%`
Input Features: Heart Rate (bpm), SpO₂ (%)
Trained In: `train_model.ipynb`

5. 🧪 Installation

    1. Clone the repository 

    git clone https://github.com/yourusername/Final_sleep_apnea_project.git
    cd Final_sleep_apnea_project

    2. Create virtual environment

    python -m venv venv
    source venv/bin/activate  # or venv\Scripts\activate on Windows

    3. Install dependencies
    
    pip install -r requirements.txt

    4. Run the application

    python app.py


6. 🌐 Render Deployment

    This project is deployable for free using Render

    1. Push Code to GitHub

    2. Add this render.yaml file to root:
        services:
        - type: web
            name: sleep-apnea-detector
            env: python
            buildCommand: "pip install -r requirements.txt"
            startCommand: "python app.py"
            plan: free
            autoDeploy: true

    3. Deploy

        Go to https://render.com

        Click New Web Service

        Connect your GitHub Repo

        Render auto-detects render.yaml and deploys 🎉

📌 Status

    🚧 This project is currently under active development.

    Future goals include smartwatch data integration, Enable cloud-based storage of patient health records and Generate visual health reports including vital trends and apnea predictions.
