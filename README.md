# Lead Manager – QA Automation

**Assignment:** [QA Lead Assignment (Google Docs)](https://docs.google.com/document/d/1Zs8TqjFaUkfZte4_gy4ZlQYEzVJ_bAF5hrkQCzMwAxA/edit?usp=sharing)

**UI:** https://v0-lead-manager-app.vercel.app  
**API:** https://v0-lead-manager-app.vercel.app/api

---

## Prerequisites

- **Python 3.10 or 3.11** (recommended; 3.8+ may work).  
  The `page` fixture used in UI tests comes from the **pytest-playwright** plugin; run tests with the same Python/venv where you installed it.

---

## Setup

```bash
python3 -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
playwright install
```

**Note:** `playwright install` downloads browser binaries (Chromium, etc.). Required before running UI tests. If you see "Executable doesn't exist", run it again with the venv activated.

---

## Run tests


**UI (Login → Create Lead → List Lead):**  
The browser window opens by default (headed mode). To run without opening the browser, add `--headed=false`.
```bash
python -m pytest ui_automation/ -v
```

**API:**
```bash
python -m pytest api_tests/ -v
```

---

## Tools

- **UI:** Python, Playwright, pytest, pytest-playwright
- **API:** Python, pytest, requests

---

## Docs

**Manual test plan (Excel):** `Testplan_Lead_Manager.xlsx` – manual test cases for the user flow:
Login → Create Lead → List Lead