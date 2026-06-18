from __future__ import annotations

from typing import Any


class ControllerPipeline:
    """Simple sample pipeline that demonstrates the controller structure."""

    def __init__(self, config: dict[str, Any]):
        self.config = config

    def run(self) -> dict[str, Any]:
        return {
            "status": "ok",
            "mode": self.config.get("mode", "default"),
            "message": "Controller pipeline executed successfully.",
        }
