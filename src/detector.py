from models import SensorReading


class FaultDetector:

    def check(self, reading):

        faults = []

        if reading.temperature > 90:
            faults.append("OVERHEATING")

        if reading.vibration > 6:
            faults.append("HIGH VIBRATION")

        if reading.rpm < 700:
            faults.append("LOW RPM")

        return faults