from __future__ import annotations


class SensorManager:
    """Placeholder sensor manager for camera and hardware inputs."""

    def read(self) -> dict[str, str]:
        return {"status": "idle", "source": "simulated"}
