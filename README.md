# VeriCart 🛒
### E-Commerce UI Automation Testing Framework

![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python&logoColor=white)
![Playwright](https://img.shields.io/badge/Playwright-Automation-2EAD33?logo=playwright&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-Testing-0A9EDC?logo=pytest&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-CI/CD-2088FF?logo=githubactions&logoColor=white)

**VeriCart** is a web UI automation testing project built with **Python, Playwright, and Pytest**. It automates essential e-commerce user workflows on [SauceDemo](https://www.saucedemo.com/), including authentication, product interactions, shopping cart operations, and checkout.

The project follows the **Page Object Model (POM)** design pattern to create reusable, maintainable, and organized automation code. GitHub Actions is integrated to execute the test suite automatically whenever changes are pushed or pull requests are created.

---

## 🎯 Project Objectives

- Automate important e-commerce user workflows.
- Practice browser automation using Playwright with Python.
- Implement the Page Object Model for better test organization.
- Validate application behavior through automated test cases.
- Integrate continuous testing using GitHub Actions.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Programming language |
| Playwright | Browser automation |
| Pytest | Test execution and assertions |
| Git & GitHub | Version control |
| GitHub Actions | Continuous Integration |
| SauceDemo | Application under test |

## ✨ Features & Test Coverage

The project currently includes **9 automated test cases**.

| Test Scenario | Description |
|---|---|
| Homepage | Verifies that the application homepage loads correctly |
| Valid Login | Checks successful authentication |
| Invalid Login | Validates error handling for incorrect credentials |
| Product Listing | Verifies that products and prices are displayed |
| Add to Cart | Checks whether a product can be added to the cart |
| Cart Verification | Validates product name and price in the cart |
| Remove from Cart | Verifies product removal and empty cart state |
| Checkout Validation | Checks required customer information validation |
| Successful Checkout | Validates successful order completion |

## 🏗️ Project Architecture

VeriCart uses the **Page Object Model (POM)** design pattern.

POM separates page-specific locators and interactions from test logic. Each application page is represented by a Python class, making the automation framework easier to maintain and extend.

### Directory Structure

```text
VeriCart/
│
├── .github/
│   └── workflows/
│       └── playwright-tests.yml
│
├── playwright-python/
│   │
│   ├── pages/
│   │   ├── __init__.py
│   │   ├── login_page.py
│   │   ├── inventory_page.py
│   │   ├── cart_page.py
│   │   └── checkout_page.py
│   │
│   ├── tests/
│   │   ├── test_homepage.py
│   │   ├── test_login.py
│   │   ├── test_invalid_login.py
│   │   ├── test_products.py
│   │   ├── test_cart.py
│   │   ├── test_cart_verification.py
│   │   ├── test_remove_from_cart.py
│   │   ├── test_checkout.py
│   │   └── test_order_confirmation.py
│   │
│   ├── conftest.py
│   └── requirements.txt
│
└── README.md
```

### Page Objects

| Page Class | Responsibility |
|---|---|
| `LoginPage` | Login page navigation, authentication, and error messages |
| `InventoryPage` | Product listing, product interactions, and cart navigation |
| `CartPage` | Cart item verification, removal, and checkout navigation |
| `CheckoutPage` | Customer information, checkout validation, and order confirmation |

The `conftest.py` file provides a reusable Pytest fixture that launches a Chromium browser and creates a page for test execution.

## ⚙️ Getting Started

### Prerequisites

Make sure you have the following installed:

- Python 3.10 or later
- Git
- A code editor such as VS Code

### 1. Clone the Repository

```bash
git clone https://github.com/jahnavist04/VeriCart.git
```

### 2. Navigate to the Project Directory

```bash
cd VeriCart/playwright-python
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it:

**Windows:**
```bash
.venv\Scripts\activate
```

**Linux / macOS:**
```bash
source .venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Install Playwright Chromium

```bash
playwright install chromium
```

For Linux CI environments, install browser dependencies with:

```bash
playwright install --with-deps chromium
```

### 6. Run the Tests

Execute the complete test suite:

```bash
pytest -v
```

Run an individual test file:

```bash
pytest tests/test_login.py -v
```

## 🔄 Continuous Integration with GitHub Actions

VeriCart uses GitHub Actions to automate test execution.

The workflow is configured in:

`.github/workflows/playwright-tests.yml`

### CI Pipeline

1. Checks out the repository.
2. Sets up the Python environment.
3. Installs project dependencies.
4. Installs Chromium and its dependencies.
5. Executes the Pytest suite.
6. Reports the test execution result.

The workflow runs on pushes to `main` and `pom-implementation`, pull requests targeting `main`, and manual workflow dispatches.

**CI validation:** All 9 automated tests passed successfully in the verified GitHub Actions run.

## 🧪 Application Under Test

**Website:** [SauceDemo](https://www.saucedemo.com/)

The project uses the publicly available SauceDemo testing application.

Standard test credentials:

```text
Username: standard_user
Password: secret_sauce
```

These are demonstration credentials provided by the test application.

## 💡 Key Learnings

Through this project, I gained practical experience with:

- Browser automation using Playwright and Python.
- Writing and organizing automated test cases with Pytest.
- Implementing the Page Object Model design pattern.
- Working with locators, browser navigation, and UI assertions.
- Validating positive and negative application scenarios.
- Managing code changes through Git and GitHub.
- Integrating automated tests into a CI workflow using GitHub Actions.
- Debugging test failures using CI execution logs.

## 🚀 Future Improvements

- Add API testing and response validation.
- Introduce data-driven testing with multiple test inputs.
- Add screenshot capture and test failure reporting.
- Expand coverage for sorting, filtering, and additional checkout scenarios.
- Integrate HTML test reports.

## 👩‍💻 Author

**Jahnavi S T**

Data Science and Engineering Student | Aspiring Software Test Engineer

[GitHub](https://github.com/jahnavist04)

---

*Built as a hands-on project to explore practical UI automation, test architecture, and continuous integration.*
