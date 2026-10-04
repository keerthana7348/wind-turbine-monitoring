import pandas as pd
from models import SensorReading
from detector import FaultDetector


data = pd.read_csv("data/turbine_data.csv")

detector = FaultDetector()

print("Wind Turbine Monitoring System")
print("--------------------------------")

for _, row in data.iterrows():

    reading = SensorReading(
        temperature=row["temperature"],
        vibration=row["vibration"],
        rpm=row["rpm"],
        wind_speed=row["wind_speed"]
    )

    faults = detector.check(reading)

    print(
        f"\nTemperature: {reading.temperature}°C | "
        f"Vibration: {reading.vibration} | "
        f"RPM: {reading.rpm} | "
        f"Wind: {reading.wind_speed} m/s"
    )

    if faults:
        print("⚠️ Faults:", ", ".join(faults))
    else:
        print("✅ Normal")