import streamlit as st
import pandas as pd


# Load data
data = pd.read_csv("data/turbine_data.csv")


# Fault detection
overheating = data["temperature"] > 90
high_vibration = data["vibration"] > 6
low_rpm = data["rpm"] < 700


# Page title
st.set_page_config(
    page_title="Wind Turbine Monitoring",
    page_icon="🌬️",
    layout="wide"
)

st.title("🌬️ Wind Turbine Monitoring System")
st.write("Real-time style monitoring using simulated turbine sensor data.")


# Latest reading
latest = data.iloc[-1]


# Sensor values
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Temperature",
        f"{latest['temperature']} °C"
    )

with col2:
    st.metric(
        "Vibration",
        f"{latest['vibration']}"
    )

with col3:
    st.metric(
        "RPM",
        f"{int(latest['rpm'])}"
    )

with col4:
    st.metric(
        "Wind Speed",
        f"{latest['wind_speed']} m/s"
    )


# Overall status
total_faults = (
    overheating.sum()
    + high_vibration.sum()
    + low_rpm.sum()
)

st.subheader("Turbine Status")

if total_faults == 0:
    st.success("✅ TURBINE OPERATING NORMALLY")
else:
    st.warning("⚠️ ATTENTION REQUIRED")


# Fault summary
st.subheader("Fault Summary")

f1, f2, f3 = st.columns(3)

with f1:
    st.metric(
        "Overheating",
        int(overheating.sum())
    )

with f2:
    st.metric(
        "High Vibration",
        int(high_vibration.sum())
    )

with f3:
    st.metric(
        "Low RPM",
        int(low_rpm.sum())
    )


# Temperature chart
st.subheader("🌡️ Temperature")

st.line_chart(
    data["temperature"]
)


# Vibration chart
st.subheader("📳 Vibration")

st.line_chart(
    data["vibration"]
)


# RPM chart
st.subheader("⚙️ RPM")

st.line_chart(
    data["rpm"]
)


# Wind speed chart
st.subheader("💨 Wind Speed")

st.line_chart(
    data["wind_speed"]
)


# Raw data
st.subheader("Sensor Data")

st.dataframe(data)
# Fault details

st.subheader("🚨 Fault Details")

fault_data = data[
    (data["temperature"] > 90) |
    (data["vibration"] > 6) |
    (data["rpm"] < 700)
].copy()

if len(fault_data) > 0:
    st.dataframe(fault_data)

    csv = fault_data.to_csv(index=False)

    st.download_button(
        label="📥 Download Fault Data",
        data=csv,
        file_name="wind_turbine_faults.csv",
        mime="text/csv"
    )

else:
    st.success("No faults detected.")