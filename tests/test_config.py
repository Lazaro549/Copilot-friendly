from app.config import load_config


def test_config_loads_default_settings():
    config = load_config()
    assert isinstance(config, dict)
    assert config.get("mode") == "default"
