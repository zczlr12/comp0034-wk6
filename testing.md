A collection of notes!


## Test the Flask routes from a browser using Selenium Webdriver and pytest

To test from the browser you will use a combination of:

- [Flask test client](https://flask.palletsprojects.com/en/3.0.x/testing/#fixtures) to create a running Flask app in a
  Pytest fixture
- [Selenium webdriver](https://www.selenium.dev/documentation/webdriver/) to launch and navigate the browser interface (
  i.e. to simulate user clicks and interactions)
- [Chrome driver](https://chromedriver.chromium.org/downloads) to allow Selenium to work with Chrome browser. The
  Selenium webdriver passes commands to the browser
  through the Chrome driver, and receives information back via the same route.
- [Pytest](https://docs.pytest.org/en/7.1.x/explanation/goodpractices.html#choosing-a-test-layout-import-rules) for test
  assertions

### Check Chrome driver works

You will use the Chrome browser for this tutorial, though Selenium supports a number of browsers (Firefox, Safari,
Edge).

In mid-2023, Chromium.org changed how the Chrome Driver works. Also from Selenium version 4.6 it is no longer required
to explicitly download Chrome Driver.

As a result of the above two changes, any tutorials before mid to late 2023 that explain how to set-up the Chrome driver
will be misleading.

In `test_browser.py` add the following code:

```python
from selenium import webdriver

# Create a Chrome driver
driver = webdriver.Chrome()
# Use the driver to navigate to the Google home page
driver.get("https://www.google.com/")
# Wait for 3 seconds
driver.implicitly_wait(3)
```

Run the code. It should launch Chrome, go to the Google home page and wait for 3 seconds.

## Overview of testing with Selenium WebDriver

There are 8 basic components to writing a test using Selenium. These are described in
the [Selenium documentation which you should read now](https://www.selenium.dev/documentation/webdriver/getting_started/first_script/#eight-basic-components).

Much of this will not apply for 