## Section A1: Manual Test Cases

**Application:** Sauce Demo  
**Test area:** Login, sorting, checkout and security  
**Tester:** Pranesh M

## 1. Questions and Assumptions

| ID | Area | Question for the Product Owner | Assumption if No Answer |
|---|---|---|---|
| Q1 | Login | What message should be shown when a user enters incorrect login details? | An error message should appear, and the user should remain on the login page. The message should not reveal whether the username or password was incorrect. |
| Q2 | Login | Is there any limit on the number of failed login attempts? | Invalid login details must always be rejected. No specific attempt limit or temporary lockout is assumed until the policy is confirmed. |
| Q3 | Sorting | If two products have the same price, should they appear in a particular order? | The order of products with equal prices does not matter. Tests will check the overall price order without expecting a specific order for equal-priced items. |
| Q4 | Checkout | Are there any specific rules for the postal code, such as its format or maximum length? | The postal code is required. An empty value should show an error and prevent checkout. Other format requirements need confirmation. |
| Q5 | Checkout | What should happen to the cart when the user cancels checkout? | No order should be placed. The cart items and badge count should remain unchanged. |
| Q6 | Checkout | What should the user see after successfully placing an order? | A confirmation message should be displayed, the cart should be emptied, and the cart badge should no longer show any items. |
| Q7 | Security | What should happen if a logged-out user opens a protected page directly using its URL? | The user should be redirected to the login page or denied access, and protected page content should not be accessible. |
| Q8 | Compatibility | Which browsers and screen sizes should the application support? | The latest version of Chrome on desktop will be the main test environment. A basic usability check will also be performed at a mobile viewport width of around 375 pixels. |



## 2. Manual Test Cases

| ID | Area | Type | Title | Pre-conditions | Steps | Test data | Expected result | Priority (P1–P3) | Automate? (Yes/No) and why |
|---|---|---|---|---|---|---|---|---|---|
| TC01 | Login | Positive | Log in with valid details | The login page is open. | 1. Enter a valid username. 2. Enter the password. 3. Click Login. | standard_user / secret_sauce | The user logs in successfully and the products page opens. | P1 | Yes — this is an important login smoke test. |
| TC02 | Login | Negative | Check login for a locked-out user | The login page is open. | 1. Enter the locked-out username. 2. Enter the password. 3. Click Login. | locked_out_user / secret_sauce | Login is blocked and an error message is displayed. | P1 | Yes — checks an important negative login scenario. |
| TC03 | Login | Negative | Try logging in with incorrect details | The login page is open. | 1. Enter an incorrect username. 2. Enter an incorrect password. 3. Click Login. | invalid_user / wrong_password | An error message appears, and the user stays on the login page. | P1 | Yes — checks whether invalid login details are rejected. |
| TC04 | Login | Negative | Try logging in without a username | The login page is open. | 1. Leave the username field empty. 2. Enter the password. 3. Click Login. | Empty username / secret_sauce | A validation message asks for a username, and login does not succeed. | P1 | No — Manual testing only for this assessment. Verify that submitting the login form with an empty username displays the correct validation message and prevents login. |
| TC05 | Login | Negative | Try logging in without a password | The login page is open. | 1. Enter a valid username. 2. Leave the password field empty. 3. Click Login. | standard_user / Empty password | A validation message asks for a password, and login does not succeed. | P1 | No — Manual testing only for this assessment. Verify that submitting the login form with an empty password displays the correct validation message and prevents login. |
| TC06 | Products | Positive | Sort products from A to Z | The user is logged in and the products page is open. | 1. Open the sort dropdown. 2. Select Name (A to Z). 3. Check the product names. | Name (A to Z) | Products appear in alphabetical order from A to Z. | P1 | Yes — checks product sorting. |
| TC07 | Products | Positive | Sort products from Z to A | The user is logged in and the products page is open. | 1. Open the sort dropdown. 2. Select Name (Z to A). 3. Check the product names. | Name (Z to A) | Products appear in reverse alphabetical order from Z to A. | P2 | No — Manual testing only for this assessment. Name (Z to A) sorting is considered a lower-priority scenario based on expected user usage. It will be verified manually to ensure the products are displayed in reverse alphabetical order. |
| TC08 | Products | Positive | Sort products by price from low to high | The user is logged in and the products page is open. | 1. Select Price (low to high). 2. Check the prices of all products. | Price (low to high) | All products appear in ascending price order. Products with equal prices may appear in either order. | P1 | Yes — this is a required price-sorting check. |
| TC09 | Products | Positive | Sort products by price from high to low | The user is logged in and the products page is open. | 1. Select Price (high to low). 2. Check the prices of all products. | Price (high to low) | All products appear in descending price order. Products with equal prices may appear in either order. | P1 | Yes — checks the other price-sorting option. |
| TC10 | Cart | Positive | Add two products to the cart | The user is logged in and the products page is open. | 1. Add the Sauce Labs Backpack. 2. Add the Sauce Labs Bike Light. 3. Check the cart badge. 4. Open the cart. | Sauce Labs Backpack and Sauce Labs Bike Light | The cart badge shows 2, and both products appear in the cart. | P1 | Yes — checks adding products and updating the cart count. |
| TC11 | Cart | Positive | Remove one of the two cart items | Two different products have been added to the cart. | 1. Open the cart. 2. Click Remove for one product. 3. Check the badge and remaining item. | Two products in the cart | The badge changes to 1, and only the product that was not removed remains. | P1 | Yes — this is a required cart test. |
| TC12 | Cart | Positive | Remove a product from the products page | A product has been added to the cart. | 1. Return to the products page. 2. Click Remove for the added product. 3. Check the cart badge. | Sauce Labs Backpack | The product is removed, and the badge updates or disappears if the cart is empty. | P1 | No — Manual testing only for this assessment. Verify manually that clicking Remove updates the cart badge and removes the selected product from the cart. |
| TC13 | Cart | Boundary | Open the cart when it is empty | The user is logged in and has not added any products. | 1. Open the cart. 2. Check the cart contents and badge. | Empty cart | No products are displayed, and no item-count badge appears. | P2 | Yes — checks the empty-cart state. |
| TC14 | Checkout | Positive | Complete an order with valid details | The user is logged in and has at least one product in the cart. | 1. Open the cart. 2. Click Checkout. 3. Enter the required details. 4. Click Continue. 5. Review the order. 6. Click Finish. | First name: Arun; Last name: M; Postal code: 641001 | The order is completed, and a confirmation message is displayed. | P1 | Yes — checks the complete checkout process. |
| TC15 | Checkout | Negative/Boundary | Try checkout without a first name | A product is in the cart, and the checkout information page is open. | 1. Leave First Name empty. 2. Enter the last name and postal code. 3. Click Continue. | Empty first name; M; 641001 | An error message appears, and the user cannot continue. | P1 | Yes — can be included in a parameterized test. |
| TC16 | Checkout | Negative/Boundary | Try checkout without a last name | A product is in the cart, and the checkout information page is open. | 1. Enter the first name. 2. Leave Last Name empty. 3. Enter the postal code. 4. Click Continue. | Arun; Empty last name; 641001 | An error message appears, and the user cannot continue. | P1 | Yes — can be included in the same parameterized test. |
| TC17 | Checkout | Negative/Boundary | Try checkout without a postal code | A product is in the cart, and the checkout information page is open. | 1. Enter the first and last names. 2. Leave Postal Code empty. 3. Click Continue. | Arun; M; Empty postal code | An error message appears, and the user cannot continue. | P1 | Yes — can be included in the same parameterized test. |
| TC18 | Checkout | Positive | Check the order total | The user has products in the cart and is on the order overview page. | 1. Note the subtotal. 2. Note the tax. 3. Note the total. 4. Add the subtotal and tax and compare the result. | Two products with different prices | The displayed total matches the subtotal plus tax, allowing for currency rounding. | P1 | Yes — checks the checkout calculation. |
| TC19 | Checkout | Positive | Check that the cart is empty after an order | The user has completed an order successfully. | 1. Open the cart after completing the order. 2. Check the cart contents and badge. | Completed order | The cart is empty, and no item-count badge is displayed. | P1 | Yes — checks the cart after checkout. |
| TC20 | Checkout | Positive | Cancel checkout and keep the cart unchanged | The user has added products and opened the checkout information page. | 1. Click Cancel. 2. Return to the cart. 3. Check the products and badge count. | Two products in the cart | No order is placed, and the same products remain in the cart. | P2 | Yes — checks that cancelling checkout does not change the cart. |
| TC21 | Security | Negative | Try opening the products page after logout | The user is logged in and the products page is open. | 1. Log out. 2. Enter /inventory.html in the browser address bar. 3. Press Enter. | /inventory.html after logout | The user is redirected to login or denied access. Product details should not be accessible while logged out. | P1 | Yes — checks access to a protected page after logout. |
| TC22 | Session | Positive | Refresh the products page while logged in | The user is logged in and the products page is open. | 1. Refresh the browser. 2. Wait for the page to load. 3. Check the products page. | standard_user | The page reloads successfully, and the logged-in user can still access the products. | P2 | No — Manual testing only for this assessment. Refresh the products page while logged in and verify that the page reloads correctly and the user remains able to access the products. |
| TC23 | Usability | Positive | Check the products page on a narrow screen | The user is logged in and the products page is open. | 1. Set the browser width to about 375 pixels. 2. Check the product cards, buttons and navigation. 3. Try scrolling and adding a product. | Viewport width: 375 pixels | The page remains usable, and important content and buttons do not overlap or become difficult to access. | P2 | Partly — basic checks can be automated, but the layout should also be reviewed manually. |
| TC24 | Accessibility | Positive | Use the login page with a keyboard | The login page is open. | 1. Use Tab to move between the form controls. 2. Check that the focused control is visible. 3. Enter the login details. 4. Submit using the keyboard. | standard_user / secret_sauce | The user can reach and use the login controls with the keyboard, and the current focus is visible. | P2 | Partly — keyboard actions can be automated, but a manual accessibility check is also useful. |



## 3. Exploratory Testing Charter

**Duration:** 15 minutes

**Area:** Login, products, cart and checkout

**Test account:** problem_user / secret_sauce

**Testing steps:**

1. **Minutes 0–3: Login** — Log in and check whether the products page opens properly. Look for any unusual behaviour or missing details.
2. **Minutes 3–6: Products** — Browse the products and try different sorting options. Check whether the product names, images and prices are displayed correctly.
3. **Minutes 6–10: Cart** — Add and remove products. Check whether the Remove button works and whether the cart contents and item count update correctly.
4. **Minutes 10–13: Checkout** — Try the checkout process. Check whether checkout can be started with an empty cart and whether the first name and last name fields accept input correctly.
5. **Minutes 13–15: Record findings** — Review the issues noticed during testing and record the steps to reproduce them, the expected result and the actual result.

**What I will look for:**

- Product images that do not match their product names.
- Sorting options that do not arrange products in the expected order.
- The Remove button failing to remove a product from the products page.
- Checkout being allowed to start when the cart is empty.
- The last name field not accepting input or interfering with the first name field on the checkout page.

**Actual Bugs / Findings:**

1. **Finding 1: Product Images Do Not Match Product Names** — Some product images do not correspond to the product names displayed.
2. **Finding 2: Product Sorting Options Do Not Work Correctly** — The sorting options do not arrange products in the expected order.
3. **Finding 3: Remove Button Does Not Work on the Products Page** — Selecting Remove does not behave as expected when trying to remove a product.
4. **Finding 4: Checkout Can Be Started with an Empty Cart** — The application allows the checkout process to be started even when no products have been added.
5. **Finding 5: Last Name Field Has an Input Issue** — The last name field does not accept input correctly and interferes with the first name field on the checkout page.

**Expected outcome:** I will document the issues found during the session, including how to reproduce each issue and the difference between the actual and expected behaviour. These findings will help identify areas that need further investigation and testing.


## 4. Test Strategy

I would automate the main user flows with Selenium, such as login, login validation, product sorting, adding and removing products, checkout validation, order total calculation, and checking access to the products page after logout. Because these tests are run often, automating them can save time and help catch problems early.

If the application has an API, I would validate backend functionality such as login validation, cart updates, order processing, and price calculations at the API level. Unit tests would be useful to test individual functions e.g. calculating the order total, validating checkout details.

I would still keep exploratory testing, visual checks for product images and page layout, keyboard accessibility and general usability checks as manual tests.

The biggest risk left is that UI tests alone cannot validate that backend data and order processing are always correct. I would tell the client about this risk and suggest API and unit test coverage where applicable.