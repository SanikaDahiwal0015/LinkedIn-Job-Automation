from playwright.sync_api import Page

def login(page: Page, email: str, password: str):
    print("🌐 Opening LinkedIn login page...")

    page.goto("https://www.linkedin.com/login")

    # Wait for the page to load
    page.wait_for_load_state("networkidle")

    # Fill credentials
    page.locator("#username").fill(email)
    page.locator("#password").fill(password)

    print("✅ Credentials entered")

    # Click Sign In
    page.locator("button[type='submit']").click()

    print("🔐 Sign In clicked")

    # Wait a few seconds to observe the result
    page.wait_for_timeout(5000)