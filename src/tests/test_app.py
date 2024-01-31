from fastapi.testclient import TestClient

from app.main import app  # noqa

client = TestClient(app)


def test_ping():
    response = client.get("/ping/")
    assert response.status_code == 200
    assert response.json() == "pong"


def test_compensation():
    response = client.get("/compensation/")
    assert response.status_code == 200
    assert response.json() is not None


def test_compensation_query_params():
    args = (
        "?annual_vacation_in_weeks=1&"
        "total_base_salary_in_2018[gte]=5000"
        "&fields=employment_type,required_hours_per_week,total_base_salary_in_2018"
        "&sort=total_base_salary_in_2018,employment_type"
    )
    response = client.get("compensation/" + args)
    assert response.status_code == 200
    assert response.json() is not None
