import os
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright
from automation.linkedin import login

load_dotenv()

LINKEDIN_EMAIL = os.getenv("LINKEDIN_EMAIL")
LINKEDIN_PASSWORD = os.getenv("LINKEDIN_PASSWORD")

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            slow_mo=300
        )

        page = browser.new_page(
            viewport={"width": 1440, "height": 900}
        )

        login(page, LINKEDIN_EMAIL, LINKEDIN_PASSWORD)

        input("Press Enter to close the browser...")

        browser.close()

if __name__ == "__main__":
    main()