from __future__ import annotations

from app.config import load_config
from controller.pipeline import ControllerPipeline


def main() -> None:
    config = load_config()
    pipeline = ControllerPipeline(config)
    result = pipeline.run()
    print(result)


if __name__ == "__main__":
    main()
