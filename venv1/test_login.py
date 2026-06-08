from playwright.sync_api import Page


# Valid Password
def test_valid_login(page: Page):

    page.goto("https://practicetestautomation.com/practice-test-login/")

    page.fill("#username", "student")
    page.fill("#password", "Password123")

    page.click("#submit")

    assert "Logged In Successfully" in page.text_content("body")
# Invalid Password
def test_invalid_password(page: Page):

    page.goto("https://practicetestautomation.com/practice-test-login/")

    page.fill("#username", "student")
    page.fill("#password", "wrong123")

    page.click("#submit")

    assert "Your password is invalid!" in page.text_content("#error")

# Invalid Username
def test_invalid_username(page: Page):

    page.goto("https://practicetestautomation.com/practice-test-login/")

    page.fill("#username", "wronguser")
    page.fill("#password", "Password123")

    page.click("#submit")

    assert "Your username is invalid!" in page.text_content("#error")

# Both Username and Password Invalid
def test_both_invalid(page: Page):

    page.goto("https://practicetestautomation.com/practice-test-login/")

    page.fill("#username", "wronguser")
    page.fill("#password", "wrong123")

    page.click("#submit")

    assert "Your username is invalid!" in page.text_content("#error")

# Blank Username and Valid Password
def test_blank_username(page: Page):

    page.goto("https://practicetestautomation.com/practice-test-login/")

    page.fill("#password", "Password123")

    page.click("#submit")

    assert page.locator("#error").is_visible()


# Blank Password and Valid Username
def test_blank_password(page: Page):

    page.goto("https://practicetestautomation.com/practice-test-login/")

    page.fill("#username", "student")

    page.click("#submit")

    assert page.locator("#error").is_visible()

# Blank Username and Invalid Password
def test_blank_username_invalid_password(page: Page):

    page.goto("https://practicetestautomation.com/practice-test-login/")

    page.fill("#password", "wrong123")

    page.click("#submit")

    assert page.locator("#error").is_visible()


# Blank Password and Invalid Username
def test_blank_password_invalid_username(page: Page):

    page.goto("https://practicetestautomation.com/practice-test-login/")

    page.fill("#username", "wronguser")

    page.click("#submit")

    assert page.locator("#error").is_visible()


# Both Blank
def test_both_blank(page: Page):

    page.goto("https://practicetestautomation.com/practice-test-login/")

    page.click("#submit")

    assert page.locator("#error").is_visible()

