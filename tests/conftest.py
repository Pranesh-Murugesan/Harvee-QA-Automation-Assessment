import os
import pytest
from selenium import webdriver


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    setattr(item, "rep_" + report.when, report)


@pytest.fixture
def driver(request):

    options = webdriver.ChromeOptions()

    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False,
        "profile.default_content_setting_values.notifications": 2
    }

    options.add_experimental_option("prefs", prefs)

    browser = webdriver.Chrome(options=options)
    browser.maximize_window()

    yield browser

    report = getattr(request.node, "rep_call", None)

    if report and report.failed:
        os.makedirs("screenshots", exist_ok=True)
        browser.save_screenshot(
            os.path.join("screenshots", request.node.name + ".png")
        )

    browser.quit()