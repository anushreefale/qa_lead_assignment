"""
API tests for GET /api/leads and POST /api/leads.
Covers successful requests and authorization (with/without token).
"""
import time
import requests

API_BASE = "https://v0-lead-manager-app.vercel.app/api"


def _token():
    """Return a valid JWT by logging in."""
    r = requests.post(
        f"{API_BASE}/login",
        json={"email": "admin@company.com", "password": "Admin@123"},
        headers={"Content-Type": "application/json"},
        timeout=10,
    )
    r.raise_for_status()
    return r.json()["token"]


def test_get_leads_ok():
    """GET /leads with valid token returns 200."""
    r = requests.get(
        f"{API_BASE}/leads",
        headers={"Authorization": f"Bearer {_token()}"},
        timeout=10,
    )
    assert r.status_code == 200


def test_get_leads_no_token():
    """GET /leads without token returns 401."""
    r = requests.get(f"{API_BASE}/leads", timeout=10)
    assert r.status_code == 401


def test_create_lead_ok():
    """POST /leads with valid token and payload returns 200 or 201."""
    r = requests.post(
        f"{API_BASE}/leads",
        headers={"Authorization": f"Bearer {_token()}", "Content-Type": "application/json"},
        json={
            "name": "API Lead",
            "email": f"api_{int(time.time())}@example.com",
            "priority": "Medium",
            "status": "New",
            "isQualified": False,
            "emailOptIn": False,
            "notes": "",
        },
        timeout=10,
    )
    assert r.status_code in (200, 201)


def test_create_lead_no_token():
    """POST /leads without token returns 401."""
    r = requests.post(
        f"{API_BASE}/leads",
        headers={"Content-Type": "application/json"},
        json={"name": "X", "email": "x@x.com", "priority": "Medium", "status": "New"},
        timeout=10,
    )
    assert r.status_code == 401
