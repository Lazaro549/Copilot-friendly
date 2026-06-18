# Jetson AI Controller

A modular edge-AI controller for robotics and embedded systems. This project is designed to run inference, manage sensor pipelines, and expose a simple interface for telemetry and control on Jetson-class hardware.

## Features
- Config-driven runtime settings
- Modular controller pipeline
- Sample inference and telemetry hooks
- CLI entry point for local development
- Testable architecture for fast iteration

## Project layout

```text
jetson-ai-controller/
├── app/            # Application entry points and config
├── controller/     # Core pipeline, inference, and control logic
├── config/         # YAML configuration files
├── tests/          # Unit and integration tests
├── docs/           # Architecture and deployment notes
└── scripts/        # Setup and runtime helpers
```

## Quick start

1. Create and activate a virtual environment.
2. Install dependencies:

   ```bash
   pip install -e "."
   ```

3. Run the sample app:

   ```bash
   python -m app.main
   ```

4. Run tests:

   ```bash
   pytest
   ```

## Configuration

The runtime settings are loaded from [config/settings.yaml](config/settings.yaml).

## Configuration

The runtime settings are loaded from [config/settings.yaml](config/settings.yaml).

## Development notes
- Use `pytest` for tests.
- Keep controller logic isolated from CLI and I/O concerns.
- Prefer small, composable modules.

## 💸 Donations

- 🇦🇷 ARS (Argentina)  
  Alias: `lazaro.503.alaba.mp`

- 🌎 USD (local transfers within Argentina only)  
  Alias: `ahogada.duras.foca`
