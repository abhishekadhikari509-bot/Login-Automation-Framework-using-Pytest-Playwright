# Login-Automation-Framework-using-Pytest-Playwright
# 🚀 Login Automation Framework using Pytest & Playwright

A scalable and maintainable Login Automation Framework built using **Python**, **Pytest**, and **Microsoft Playwright** following the **Page Object Model (POM)** design pattern.

This framework automates login functionality testing and demonstrates industry-standard automation practices including reusable page objects, fixtures, reporting, and test organization. Pytest and Playwright are widely used together for reliable browser automation and maintainable test suites. :contentReference[oaicite:0]{index=0}

---

## 📌 Features

- ✅ Pytest Test Framework
- ✅ Playwright Browser Automation
- ✅ Page Object Model (POM)
- ✅ Reusable Fixtures
- ✅ Cross-browser Support
- ✅ Screenshot Capture on Failure
- ✅ HTML Test Reports
- ✅ Easy Test Maintenance
- ✅ Scalable Project Structure

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|----------|
| Python | Programming Language |
| Pytest | Test Runner |
| Playwright | Browser Automation |
| HTML Reports | Test Reporting |
| Git & GitHub | Version Control |

---

## 📂 Project Structure

```text
Login-Automation-Framework-using-Pytest-Playwright
│
├── pages/
│   └── login_page.py
│
├── tests/
│   └── test_login.py
│
├── utils/
│   └── config.py
│
├── screenshots/
│
├── reports/
│
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/abhishekadhikari509-bot/Login-Automation-Framework-using-Pytest-Playwright.git
cd Login-Automation-Framework-using-Pytest-Playwright
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Mac/Linux

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Install Playwright Browsers

```bash
playwright install
```

---

## ▶️ Running Tests

### Run All Tests

```bash
pytest -v
```

### Run Specific Test

```bash
pytest tests/test_login.py -v
```

### Generate HTML Report

```bash
pytest --html=reports/report.html --self-contained-html
```

---

## 📊 Test Scenarios Covered

### Login Module

- Valid Login
- Invalid Username
- Invalid Password
- Blank Username
- Blank Password
- Blank Credentials
- Error Message Validation
- UI Element Verification

---

## 📸 Screenshots

Screenshots are automatically captured for failed test cases and stored in the `screenshots/` directory.

---

## 🔥 Framework Highlights

- Clean and modular architecture
- Easy to add new test cases
- Reusable Page Objects
- Suitable for beginners and enterprise-level projects
- Supports regression and smoke testing

---

## 🎯 Future Enhancements

- Allure Reporting
- Jenkins CI/CD Integration
- Parallel Execution
- Data-Driven Testing
- Excel/CSV Test Data Support
- API Testing Integration

---

## 👨‍💻 Author

**Abhishek Adhikari**

QA Automation Engineer | Playwright | Pytest | Python | Manual Testing

GitHub:
:contentReference[oaicite:1]{index=1}

LinkedIn:
(Add your LinkedIn profile URL here)

---

## ⭐ Support

If you found this project useful:

- Star the repository ⭐
- Fork the repository 🍴
- Share feedback and suggestions 💡

Happy Testing! 🚀
