import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data/turbine_data.csv")

reading = range(len(data))


# 1. Temperature
plt.figure(figsize=(10, 5))

plt.plot(reading, data["temperature"], marker="o", label="Temperature")

plt.axhline(
    90,
    linestyle="--",
    label="Temperature Limit"
)

faults = data["temperature"] > 90

plt.scatter(
    [i for i, x in enumerate(faults) if x],
    data.loc[faults, "temperature"],
    marker="x",
    s=100,
    label="Overheating"
)

plt.title("Wind Turbine Temperature Monitoring")
plt.xlabel("Sensor Reading")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.grid()
plt.savefig("reports/temperature.png")
plt.show()


# 2. Vibration
plt.figure(figsize=(10, 5))

plt.plot(reading, data["vibration"], marker="o", label="Vibration")

plt.axhline(
    6,
    linestyle="--",
    label="Vibration Limit"
)

faults = data["vibration"] > 6

plt.scatter(
    [i for i, x in enumerate(faults) if x],
    data.loc[faults, "vibration"],
    marker="x",
    s=100,
    label="High Vibration"
)

plt.title("Wind Turbine Vibration Monitoring")
plt.xlabel("Sensor Reading")
plt.ylabel("Vibration")
plt.legend()
plt.grid()
plt.savefig("reports/vibration.png")
plt.show()


# 3. RPM
plt.figure(figsize=(10, 5))

plt.plot(reading, data["rpm"], marker="o", label="RPM")

plt.axhline(
    700,
    linestyle="--",
    label="Minimum RPM"
)

faults = data["rpm"] < 700

plt.scatter(
    [i for i, x in enumerate(faults) if x],
    data.loc[faults, "rpm"],
    marker="x",
    s=100,
    label="Low RPM"
)

plt.title("Wind Turbine RPM Monitoring")
plt.xlabel("Sensor Reading")
plt.ylabel("RPM")
plt.legend()
plt.grid()
plt.savefig("reports/rpm.png")
plt.show()


# 4. Wind Speed
plt.figure(figsize=(10, 5))

plt.plot(
    reading,
    data["wind_speed"],
    marker="o",
    label="Wind Speed"
)

plt.title("Wind Turbine Wind Speed")
plt.xlabel("Sensor Reading")
plt.ylabel("Wind Speed (m/s)")
plt.legend()
plt.grid()
plt.savefig("reports/wind_speed.png")
plt.show()