import gradio as gr
import pandas as pd
import joblib

# Load model & scaler
model = joblib.load("apnea_model_hr_spo2_only.pkl")
scaler = joblib.load("apnea_scaler_hr_spo2_only.pkl")

# Prediction function
def predict_apnea(hr, spo2):
    try:
        X_input = pd.DataFrame([[hr, spo2]], columns=['heart_rate', 'spo2'])
        X_scaled = scaler.transform(X_input)
        pred = model.predict(X_scaled)[0]
        return "😷 Apnea Detected" if pred == 1 else "✅ Normal Breathing"
    except Exception as e:
        return f"❌ Error: {e}"

# Gradio interface
demo = gr.Interface(
    fn=predict_apnea,
    inputs=[
        gr.Number(label="Heart Rate (bpm)", value=70),
        gr.Number(label="SpO₂ (%)", value=95)
    ],
    outputs=gr.Textbox(label="Prediction"),
    title="🩺 Sleep Apnea Detection (HR + SpO₂)",
    description="Enter heart rate and SpO₂ values to detect apnea."
)

demo.launch()
