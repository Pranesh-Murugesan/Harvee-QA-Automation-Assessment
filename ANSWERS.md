# Section B — Answers

## B1. Review AI-Generated Code

### Problems Identified

1. **Weak assertion:** The test only checks whether the total exists. It does not verify that the calculation is correct.
2. **Incorrect product selection:** `text=Add to cart` may match multiple buttons instead of selecting a specific product.
3. **Fixed wait:** `waitForTimeout(3000)` adds an unnecessary fixed delay and may still fail if the page takes longer to load.
4. **No subtotal verification:** The test does not check whether the subtotal matches the selected products' prices.
5. **No tax verification:** The test does not check the tax amount.
6. **No cart verification:** The test does not confirm that the intended products were successfully added to the cart.
7. **Hardcoded values:** The URL and login credentials are directly written in the test instead of using configuration values.

### Rewritten Test

I used the existing Selenium and Pytest automation test from Section A to verify that the subtotal plus tax equals the displayed total.

```python
from config import BASE_URL, STANDARD_USERNAME, STANDARD_PASSWORD
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_TC18_subtotal_plus_tax_equals_total(driver):
    driver.get(BASE_URL)

    login_page = LoginPage(driver)
    login_page.login(STANDARD_USERNAME, STANDARD_PASSWORD)

    product_page = ProductPage(driver)
    product_page.add_products(2)
    product_page.open_cart()

    cart_page = CartPage(driver)
    assert cart_page.get_product_count() == 2

    checkout_page = CheckoutPage(driver)
    checkout_page.click_checkout()
    checkout_page.enter_customer_details("Test", "User", "641001")
    checkout_page.click_continue()

    subtotal = checkout_page.get_subtotal()
    tax = checkout_page.get_tax()
    total = checkout_page.get_total()

    assert round(subtotal + tax, 2) == round(total, 2)
```

### Explanation

This test uses the existing Page Object Model and configuration from Section A. Instead of checking only whether the total is displayed, it verifies that the subtotal plus tax equals the final total.

## B2. Test an AI Feature

**Selected Scenario: Test Case Generator**

I selected the test case generator because it is related to my automation testing work. The tool converts a user story into test cases in JSON format. I would check the following four things to make sure the generated test cases are useful and correct.

**1. Test Coverage**

I would check whether the AI covers the important positive, negative, and boundary scenarios mentioned in the user story.

**Scoring:** By rubric — I would give a score based on how many important scenarios are covered.

**2. Invented Requirements**

I would check whether the AI adds any test cases based on requirements that are not mentioned in the user story.

**Scoring:** By human review — I would compare the generated test cases with the original user story to identify any unsupported requirements.

**3. Duplicate Test Cases**

I would check whether the AI generates multiple test cases that test the same functionality unnecessarily.

**Scoring:** Automatically — I would compare the test case descriptions and expected results to identify possible duplicates.

**4. JSON Format**

I would check whether the generated output follows the required JSON format and contains all the necessary fields.

**Scoring:** Automatically — I would use a JSON parser to check whether the output is valid and can be processed by the test management tool.

These checks would help me confirm that the AI generates relevant test cases, avoids unsupported requirements, reduces duplication, and produces output that can be used by the testing team.

## B3. Defect Report

**Title:** Price sorting shows products in the wrong order in Release 4.2.0

**Environment:**
- Application: Sauce Demo
- Version: 4.2.0
- Browser: Google Chrome

**Steps to Reproduce:**
1. Open the Sauce Demo website.
2. Log in using a valid username and password.
3. Go to the Products page.
4. Select **Price (low to high)** from the sorting dropdown.
5. Check the order of the product prices.

**Expected Result:** Products should be displayed from the lowest price to the highest price.

**Actual Result:** The product priced at $29.99 appears before the product priced at $15.99.

**Severity:** Major (S2), because the sorting feature is not working correctly and users may not see the cheaper products first. The issue occurs on every run since version 4.2.0.

**Evidence to Attach:**
- Screenshot showing the incorrect price order.
- Test execution results showing the issue.

## B4. Message to the Client

Hi, I wanted to share an update before Friday’s release. During testing, I found an issue with price sorting, where products are not displayed in the correct price order. I also noticed that one checkout test fails occasionally, even though it passes when run again.

I recommend fixing the sorting issue before release and investigating the checkout failure to make sure the checkout process is reliable.

As an alternative, we could postpone the release briefly to fix and retest these issues. If Friday’s release is necessary, we could consider releasing only after reviewing the impact of both issues and getting approval from the team.

Please let me know which option you would prefer. I’m happy to help with retesting once the fixes are ready.