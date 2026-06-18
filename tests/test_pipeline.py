from controller.pipeline import ControllerPipeline


def test_pipeline_run_returns_expected_fields():
    result = ControllerPipeline({"mode": "test"}).run()
    assert result["status"] == "ok"
    assert result["mode"] == "test"
    assert "message" in result
