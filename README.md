# LinkedIn Job Automation

A Python-based browser automation project built using **Playwright** that demonstrates launching a Chromium browser and navigating to the LinkedIn login page. This project serves as the foundation for a job automation workflow that can later be extended with authentication, job search, recruiter data extraction, and email automation.

> **Project Status:** Initial Prototype

---

# Features

- Launches Chromium browser using Playwright
- Automatically opens the LinkedIn login page
- Uses Python virtual environment
- Loads environment variables using `.env`
- Modular project structure
- Ready for future feature expansion

---

# Tech Stack

- Python 3.12+
- Playwright
- python-dotenv

---

# Project Structure

```
LinkedInJobAutomation/
│
├── automation/
│   ├── __init__.py
│   ├── linkedin.py
│   ├── gmail.py
│   ├── parser.py
│   └── utils.py
│
├── logs/
│
├── resumes/
│
├── screenshots/
│
├── .env
├── .gitignore
├── main.py
├── requirements.txt
├── README.md
└── venv/
```

---

# Installation

## 1. Clone Repository

```bash
git clone <repository-url>
cd LinkedInJobAutomation
```

---

## 2. Create Virtual Environment

Windows

```bash
python -m venv venv
```

Activate Virtual Environment

```bash
.\venv\Scripts\Activate.ps1
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

or

```bash
pip install playwright
pip install python-dotenv
```

---

## 4. Install Playwright Browser

```bash
playwright install chromium
```

---

# Environment Variables

Create a `.env` file in the root directory.

Example:

```env
LINKEDIN_EMAIL=your_linkedin_email
LINKEDIN_PASSWORD=your_linkedin_password

GMAIL_EMAIL=your_gmail_email
GMAIL_PASSWORD=your_gmail_password
```

---

# Running the Project

```bash
python main.py
```

---

# Current Workflow

```
Start
   │
   ▼
Load Environment Variables
   │
   ▼
Launch Chromium Browser
   │
   ▼
Open LinkedIn Login Page
   │
   ▼
Wait for User Interaction
   │
   ▼
Close Browser
   │
   ▼
End
```

---

# Dependencies

requirements.txt

```text
playwright
python-dotenv
```

---

# Current Progress

## Completed

- Python project setup
- Virtual environment configuration
- Playwright installation
- Chromium browser installation
- Browser automation
- Environment variable configuration
- LinkedIn login page navigation
- Basic modular project structure

---

## Planned Features

- Automatic LinkedIn authentication
- Search jobs using custom keywords
- Filter recent job posts
- Extract recruiter details
- Extract recruiter email addresses
- Export recruiter data to CSV
- Gmail automation
- Resume attachment
- Automatic email sending
- Logging
- Screenshots
- Error handling
- Retry mechanism

---

# Known Issues

### LinkedIn Login Automation

During development, the browser successfully launches and navigates to the LinkedIn login page. However, automatically interacting with the login form (filling credentials and signing in) was not completed.

### Reason

LinkedIn employs several security and anti-automation mechanisms that can interfere with browser automation tools. These include:

- Dynamic page rendering
- Anti-bot detection
- Browser fingerprinting
- CAPTCHA challenges
- Login verification checks
- Rate limiting
- Security validation for automated browsers

Because of these protections, Playwright may not consistently interact with the login page across different environments or accounts without additional configuration or manual verification.

---

# Future Improvements

Possible future enhancements include:

- Persistent browser sessions
- Better element detection
- Improved selector strategies
- Robust exception handling
- Logging system
- CSV/Excel export
- Gmail API integration
- Resume attachment support
- User interface (GUI)
- Headless mode support

---

# Notes

This project was developed as part of an internship assessment to demonstrate browser automation concepts using Python and Playwright.

The current implementation focuses on project setup, browser automation, and opening the LinkedIn login page. More advanced automation features are planned for future development.

**Note:** LinkedIn is a third-party platform with security mechanisms designed to protect user accounts and prevent unauthorized automation. Any future automation involving LinkedIn or other services should comply with their Terms of Service and applicable policies. This project is intended for educational and demonstration purposes.

---

# Author

**Sanika Dahiwal**

Third Year Engineering Student

Web Developer | Python | Playwright

---