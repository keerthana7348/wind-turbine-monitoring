# 🌬️ Wind Turbine Monitoring & Fault Detection System

A Python-based monitoring system that analyzes simulated wind turbine sensor data, detects abnormal operating conditions, generates fault reports, and provides an interactive Streamlit dashboard.

## 🎯 Project Objective

The objective of this project is to monitor important wind turbine parameters and identify potential faults using predefined engineering thresholds.

## 📊 Parameters Monitored

- 🌡️ Temperature
- 📳 Vibration
- ⚙️ RPM (Revolutions Per Minute)
- 💨 Wind Speed

## 🚨 Fault Detection

The system detects abnormal turbine conditions such as:

- 🔥 Overheating
- 📳 High Vibration
- ⚙️ Low RPM

## 🖥️ Dashboard

The project includes an interactive Streamlit dashboard that displays:

- Current temperature
- Vibration level
- RPM
- Wind speed
- Turbine status
- Fault summary
- Fault information

### Dashboard Preview
<img width="1721" height="641" alt="Screenshot 2026-10-04 160942" src="https://github.com/user-attachments/assets/1d1ef633-416f-44d8-a705-10b3399b80cd" />
![Uploading Screenshot 2026-10-04 160942.png…]()

![Wind Turbine Monitoring Dashboard](screenshots/dashboard.png)

## 📁 Project Structure

```text
wind-turbine-monitoring/
│
├── data/
│   └── turbine_data.csv
│
├── reports/
│   ├── temperature.png
│   ├── vibration.png
│   ├── rpm.png
│   ├── wind_speed.png
│   └── fault_report.csv
│
├── screenshots/
│   └── dashboard.png
│
├── src/
│   ├── detector.py
│   ├── main.py
│   ├── models.py
│   ├── report.py
│   └── visualize.py
│
├── tests/
│   └── test_detector.py
│
├── dashboard.py
├── pytest.ini
<img width="1721" height="641" alt="Screenshot 2026-10-04 160942" src="https://github.com/user-attachments/assets/5281532a-3fa6-4d47-9e54-2c08148e67c0" />
