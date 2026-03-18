"""
UI: Login → Create Lead → List Lead (one path).
"""
from playwright.sync_api import Page

BASE_URL = "https://v0-lead-manager-app.vercel.app"
EMAIL = "admin@company.com"
PASSWORD = "Admin@123"


def test_login_create_lead_list_lead(page: Page):
    # 1. Login
    page.goto(BASE_URL)
    page.get_by_test_id("login-email-input").fill(EMAIL)
    page.get_by_test_id("login-password-input").fill(PASSWORD)
    page.get_by_test_id("login-submit-btn").click()

    # 2. Wait for dashboard, open Create Lead
    page.get_by_test_id("leads-create-new-btn").wait_for(state="visible", timeout=15000)
    page.get_by_test_id("leads-create-new-btn").click()

    # 3. Fill form 
    lead_name = "Auto Lead"
    lead_email = f"autolead_@example.com"
    page.get_by_test_id("create-form-name-input").fill(lead_name)
    page.get_by_test_id("create-form-email-input").fill(lead_email)
    page.get_by_test_id("create-form-submit-btn").click()

    # 4. New lead should appear in list
    page.get_by_test_id("modal-create-lead").wait_for(state="hidden", timeout=5000)
    assert lead_name in page.content() or lead_email in page.content()
