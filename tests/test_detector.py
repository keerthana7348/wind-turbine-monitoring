from detector import FaultDetector
from models import SensorReading


def test_overheating():
    detector = FaultDetector()

    reading = SensorReading(95, 2, 1200, 10)

    faults = detector.check(reading)

    assert "OVERHEATING" in faults


def test_high_vibration():
    detector = FaultDetector()

    reading = SensorReading(70, 8, 1200, 10)

    faults = detector.check(reading)

    assert "HIGH VIBRATION" in faults


def test_low_rpm():
    detector = FaultDetector()

    reading = SensorReading(70, 2, 500, 10)

    faults = detector.check(reading)

    assert "LOW RPM" in faults


def test_normal_turbine():
    detector = FaultDetector()

    reading = SensorReading(70, 2, 1200, 10)

    faults = detector.check(reading)

    assert faults == []