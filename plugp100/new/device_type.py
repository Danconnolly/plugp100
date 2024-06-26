from enum import Enum


class DeviceType(Enum):
    Plug = "plug"
    Bulb = "bulb"
    Hub = "hub"
    Sensor = "sensor"
    Unknown = "unknown"

    @staticmethod
    def from_value(name: str) -> "DeviceType":
        """Return device type from string value."""
        for device_type in DeviceType:
            if device_type.value == name:
                return device_type
        return DeviceType.Unknown
