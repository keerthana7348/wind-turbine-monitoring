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
<img width="1721" height="641" alt="Screenshot 2026-10-04 160942" src="https://github.com/user-attachments/assets/5281532a-3fa6-4d47-9e54-2c08148e67c0" />
<img width="1729" height="549" alt="Screenshot 2026-10-04 161002" src="https://github.com/user-attachments/assets/8260847f-96d3-4e61-9171-4efa752cc7b9" />
<img width="1802" height="533" alt="Screenshot 2026-10-04 161018" src="https://github.com/user-attachments/assets/025cfe49-2180-4aa3-aa77-380973fb2b0e" />
<img width="1753" height="541" alt="Screenshot 2026-10-04 161043" src="https://github.com/user-attachments/assets/d41d95ff-c0b3-41fe-a739-63d77d576839" />
<img width="1781" height="552" alt="Screenshot 2026-10-04 161109" src="https://github.com/user-attachments/assets/feee242d-59a0-4b3b-946b-d016ee8f29c5" />
<img width="1761" height="603" alt="Screenshot 2026-10-04 161129" src="https://github.com/user-attachments/assets/4c05c52a-948b-4c31-b846-f879685090b1" />
<img width="1805" height="438" alt="Screenshot 2026-10-04 161148" src="https://github.com/user-attachments/assets/4ce9e6da-f6e9-4133-b1e3-9ccf76c1c59f" />

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







