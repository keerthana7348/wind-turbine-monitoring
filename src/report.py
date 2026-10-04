import pandas as pd


data = pd.read_csv("data/turbine_data.csv")


overheating = data["temperature"] > 90
high_vibration = data["vibration"] > 6
low_rpm = data["rpm"] < 700


print("===================================")
print("     WIND TURBINE FAULT REPORT")
print("===================================")

print("Total sensor readings:", len(data))

print("\nFault Summary")
print("-----------------------------")

print("Overheating:", overheating.sum())
print("High Vibration:", high_vibration.sum())
print("Low RPM:", low_rpm.sum())


total_faults = (
    overheating.sum()
    + high_vibration.sum()
    + low_rpm.sum()
)

print("\nTotal Faults:", total_faults)

if total_faults == 0:
    print("\nOverall Status: ✅ NORMAL")
else:
    print("\nOverall Status: ⚠️ ATTENTION REQUIRED")


report = pd.DataFrame({
    "Fault Type": [
        "Overheating",
        "High Vibration",
        "Low RPM"
    ],
    "Occurrences": [
        overheating.sum(),
        high_vibration.sum(),
        low_rpm.sum()
    ]
})

report.to_csv("reports/fault_report.csv", index=False)

print("\nReport saved to:")
print("reports/fault_report.csv")