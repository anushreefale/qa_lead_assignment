"""Shared fixtures for API tests."""
import pytest
import requests

API_BASE = "https://v0-lead-manager-app.vercel.app/api"


@pytest.fixture(scope="module")
def token():
    r = requests.post(
        f"{API_BASE}/login",
        json={"email": "admin@company.com", "password": "Admin@123"},
        headers={"Content-Type": "application/json"},
        timeout=10,
    )
    r.raise_for_status()
    return r.json()["token"]


@pytest.fixture
def auth_headers(token):
    return {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
