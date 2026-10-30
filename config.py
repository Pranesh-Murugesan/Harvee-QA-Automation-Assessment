import os

BASE_URL = os.getenv("BASE_URL", "https://www.saucedemo.com/")

STANDARD_USERNAME = os.getenv("STANDARD_USERNAME", "standard_user")
STANDARD_PASSWORD = os.getenv("STANDARD_PASSWORD", "secret_sauce")

LOCKED_USERNAME = os.getenv("LOCKED_USERNAME", "locked_out_user")