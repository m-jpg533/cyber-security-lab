# 🛡️ Cyber Security Lab (Safe Simulation)

This project is a **safe educational simulation** of a command-and-control system.

## ⚠️ Disclaimer
This project is for **learning purposes only**.
Do NOT use on unauthorized systems.

## 🚀 Features
- C2 Server (Flask)
- Client Simulation
- SOC Dashboard

## 🧪 How to Run

### 1. Deploy C2 Server (Render)
- Upload `c2_server`
- Start with:
  gunicorn server:app

### 2. Run Client
python client.py

### 3. Open Dashboard
Open `dashboard.html`

## 📡 API
- /get_command
- /set_command
- /report
- /clients
