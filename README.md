# Harvee QA Automation Assessment — Section A

## 1. Project Overview

This project contains a Selenium and Pytest automation framework for testing the Sauce Demo web application. It uses the Page Object Model (POM) to separate page interactions from test logic, making the tests easier to maintain and extend.

**Technologies used:**

- Python
- Selenium WebDriver
- Pytest
- pytest-html
- Page Object Model (POM)

## 2. Setup Instructions

**Prerequisites:** Python installed and Google Chrome available.

1. Open a terminal in the project directory.

2. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

3. Activate the environment in Windows PowerShell:

   ```powershell
   .\venv\Scripts\Activate.ps1
   ```

4. Install the dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

Selenium manages compatible browser drivers through Selenium Manager in supported environments.

## 3. Running the Tests

Run the complete test suite:

```bash
python -m pytest -v
```

Generate a self-contained HTML report:

```bash
python -m pytest -v --html=reports/report.html --self-contained-html
```

After execution, open `reports/report.html` in a browser to review the results.

Run an individual test file, for example:

```bash
python -m pytest tests/test_login.py -v
```

## 4. Manual Test Case to Automation Mapping

The table below maps the case IDs in `manual_test_case.md` to the corresponding automated tests.

Cases marked **Manual only** are not included in the current automation suite. 

| Manual Case ID | Automated Test / Coverage |
|---|---|
| TC01 | `test_TC01_standard_user_login` — Automated |
| TC02 | `test_TC02_locked_out_user_login` — Automated |
| TC03 | `test_TC03_invalid_login_credentials` — Automated |
| TC04 | Manual only — Login with an empty username |
| TC05 | Manual only — Login with an empty password |
| TC06 | `test_TC06_sort_products_name_az` — Automated |
| TC07 | Manual only — Sort products by name Z to A |
| TC08 | `test_TC08_sort_products_price_low_to_high` — Automated |
| TC09 | `test_TC09_sort_products_price_high_to_low` — Automated |
| TC10 | `test_TC10_add_two_products_and_verify_cart` — Automated |
| TC11 | `test_TC11_remove_one_product_from_cart` — Automated |
| TC12 | Manual only — Remove a product from the products page |
| TC13 | `test_TC13_empty_cart` — Automated |
| TC14 | `test_TC14_full_checkout_and_verify_total` — Automated |
| TC15 | `test_checkout_required_fields[TC15_missing_first_name]` — Automated via parameterized test |
| TC16 | `test_checkout_required_fields[TC16_missing_last_name]` — Automated via parameterized test |
| TC17 | `test_checkout_required_fields[TC17_missing_postal_code]` — Automated via parameterized test |
| TC18 | `test_TC18_subtotal_plus_tax_equals_total` — Automated |
| TC19 | `test_TC19_cart_empty_after_order` — Automated |
| TC20 | `test_TC20_cancel_checkout` — Automated |
| TC21 | `test_TC21_open_products_url_after_logout` — Automated |
| TC22 | Manual only — Refresh the products page while logged in |
| TC23 | Partly automatable — Narrow-screen usability; manual layout review required |
| TC24 | Partly automatable — Keyboard accessibility; manual focus and accessibility review required |

## 5. Framework Design

The framework follows the Page Object Model (POM), where locators and reusable browser actions are maintained in page classes. The shared browser fixture in `tests/conftest.py` creates and closes the browser for each test. Selenium explicit waits are used for dynamic page elements instead of fixed sleeps. The base URL and test credentials are maintained in `config.py` and can be overridden using environment variables. A Pytest hook captures screenshots when tests fail and saves them in the `screenshots/` folder. The `pytest-html` plugin generates an HTML report for reviewing test results. Each test is designed to set up its own required state and run independently without depending on a particular execution order.

## 6. Scaling the Framework to 200 Tests

To scale this framework to 200 tests, I would continue organizing tests by feature and maintain reusable Page Object classes to reduce duplicated code. Shared fixtures would handle browser setup and cleanup, while configuration and test data would be kept separate from test logic. Pytest markers could help run selected groups of tests, such as login, cart, or checkout. Parameterization could reduce repetitive test code for similar scenarios.

HTML reports and failure screenshots would help with debugging, and a continuous integration pipeline could run the suite automatically whenever changes are made. I would also review test independence, avoid duplicated scenarios, and keep locators and reusable actions centralized to make maintenance easier.

## 7. Test Execution Result

The full test suite was executed successfully during development, with **17 test executions passing**.

The HTML report was generated at `reports/report.html`.