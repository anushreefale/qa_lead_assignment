"""
API tests for POST /api/login.
Covers successful login, invalid password, and missing password validation.
"""
import requests

API_BASE = "https://v0-lead-manager-app.vercel.app/api"


def test_login_success():
    """Valid credentials return 200 and a token."""
    r = requests.post(
        f"{API_BASE}/login",
        json={"email": "admin@company.com", "password": "Admin@123"},
        headers={"Content-Type": "application/json"},
        timeout=10,
    )
    assert r.status_code == 200
    data = r.json()
    assert data.get("success") is True and "token" in data


def test_login_invalid_password():
    """Wrong password returns 400 or 401."""
    r = requests.post(
        f"{API_BASE}/login",
        json={"email": "admin@company.com", "password": "WrongPass"},
        headers={"Content-Type": "application/json"},
        timeout=10,
    )
    assert r.status_code in (400, 401)


def test_login_missing_password():
    """Missing password returns 400 or 422."""
    r = requests.post(
        f"{API_BASE}/login",
        json={"email": "admin@company.com"},
        headers={"Content-Type": "application/json"},
        timeout=10,
    )
    assert r.status_code in (400, 422)
