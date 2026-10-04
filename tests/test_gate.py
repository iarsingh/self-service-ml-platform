from fastapi.testclient import TestClient
from ssml.main import app

client = TestClient(app)


def test_pass_and_fail():
    good = client.post("/check", json={'project': 'churn', 'owner': 'ada', 'data_class': 'internal'}).json()
    assert good["passed"] is True
    assert good["applied"] is False
    bad = client.post("/check", json={'project': 'churn', 'owner': 'ada'}).json()
    assert bad["passed"] is False
    assert "missing_data_class" in bad["failed"]
