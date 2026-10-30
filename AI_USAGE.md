# AI Usage Disclosure

I used ChatGPT as an AI assistant to help resolve the following problems during development of the Section A automation framework.

## 1. Naming Conventions

**Problem:** I wanted clearer and more consistent names for test functions so that each test's purpose was easy to understand.

**AI Assistance:** ChatGPT suggested descriptive test names that include the test case ID and scenario, such as test_TC01_standard_user_login.

## 2.config.py — Configuration Values

**Problem:** I initially defined the base URL and test usernames/passwords directly in the configuration file and wanted a way to override them without changing the code.

**AI Assistance:** ChatGPT suggested using os.getenv() to read values from environment variables, with default values as fallbacks.

## 3. pytest.ini — Import Errors

**Problem:** I was unsure why Pytest could not locate project modules during test execution and encountered import-related issues.

**AI Assistance:** ChatGPT explained that pythonpath = . adds the project root directory to Pytest's Python import path, helping it locate modules such as config.py.

## 4.tests/conftest.py — Screenshots on Failure

**Problem:** I did not know how to automatically capture a screenshot when an automated test failed.

**AI Assistance:** ChatGPT suggested using the Pytest pytest_runtest_makereport hook to detect failures and Selenium's save_screenshot() method to save screenshots.

## 5. Test Execution — Unexpected Google Password Pop-up

**Problem:** An unexpected Google password pop-up appeared during test execution and caused tests to fail.

**AI Assistance:** I used ChatGPT to troubleshoot the pop-up and identify ways to prevent it from interrupting Selenium tests.

## 6. Documentation — Test Cases and Project Files

**Problem:** I had assessment notes and test scenarios that needed to be organized into clear project documentation.

**AI Assistance:** I used ChatGPT to help structure and document the test cases and project documentation in a clear, readable format.

## 7. Understanding the Section B Code Review

**Problem:** The code provided in the assessment used TypeScript and Playwright, which I was not familiar with because I had developed my automation framework using Python, Selenium, and Pytest.

**AI Assistance:** I used ChatGPT to understand what the given code was doing, identify its main problems, and understand the purpose of the test. I then used that explanation to rewrite the test using Selenium and Pytest, following the approach I had already used in Section A.