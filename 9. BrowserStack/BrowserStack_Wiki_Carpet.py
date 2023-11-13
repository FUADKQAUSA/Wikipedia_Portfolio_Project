from dotenv import load_dotenv
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.safari.options import Options as SafariOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from threading import Thread
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.wait import WebDriverWait
import unittest
import time
import my_key


load_dotenv()
BROWSERSTACK_USERNAME = os.environ.get("BROWSERSTACK_USERNAME") or my_key.BROWSERSTACK_USERNAME
BROWSERSTACK_ACCESS_KEY = os.environ.get("BROWSERSTACK_ACCESS_KEY") or my_key.BROWSERSTACK_ACCESS_KEY
URL = os.environ.get("URL") or "https://hub.browserstack.com/wd/hub"
BUILD_NAME = "browserstack-Cross-Browser-test"
capabilities = [
    {
        "browserName": "chrome",
        "browserVersion": "latest",
        "os": "Windows",
        "osVersion": "11",
        "sessionName": "BStack Python sample parallel-Chrome-Win10",  # test name
        "buildName": BUILD_NAME,  # Your tests will be organized within this build
    },
    {
        "browserName": "firefox",
        "browserVersion": "latest",
        "os": "Windows",
        "osVersion": "10",
        "sessionName": "BStack Python sample parallel-Firefox-Win10",
        "buildName": BUILD_NAME,
    },
    {
        "browserName": "safari",
        "browserVersion": "latest",
        "os": "OS X",
        "osVersion": "Big Sur",
        "sessionName": "BStack Python sample parallel-Safari-BigSur",
        "buildName": BUILD_NAME,
    },
    {
        "browserName": "safari",
        "browserVersion": "14.1",
        "os": "OS X",
        "osVersion": "Big Sur",
        "sessionName": "BStack Python sample parallel-Safari-BigSur",
        "buildName": BUILD_NAME,
    },
]


def get_browser_option(browser):
    switcher = {
        "chrome": ChromeOptions(),
        "firefox": FirefoxOptions(),
        "edge": EdgeOptions(),
        "safari": SafariOptions(),
    }
    return switcher.get(browser, ChromeOptions())


def run_session(cap):
    bstack_options = {
        "osVersion": cap["osVersion"],
        "buildName": cap["buildName"],
        "sessionName": cap["sessionName"],
        "userName": BROWSERSTACK_USERNAME,
        "accessKey": BROWSERSTACK_ACCESS_KEY
    }
    if "os" in cap:
        bstack_options["os"] = cap["os"]
    options = get_browser_option(cap["browserName"].lower())
    if "browserVersion" in cap:
        options.browser_version = cap["browserVersion"]
    options.set_capability('bstack:options', bstack_options)
    driver = webdriver.Remote(
        command_executor=URL,
        options=options)



    try:
        driver.get("https://www.wikipedia.org/")
        driver.maximize_window()
        driver.minimize_window()
        driver.maximize_window()

        try:
            assert "Wikipedia" in driver.title
            print(driver.title)
        except AssertionError:
            print("Title is different", driver.title)

        driver.find_element(By.XPATH, '//body/div[1]')
        driver.find_element(By.ID, 'searchInput').click()
        driver.find_element(By.ID, 'searchInput').send_keys("Carpet")
        driver.find_element(By.XPATH, '//button[contains(.,"Search")]')

        time.sleep(2)

        driver.find_element(By.XPATH, '//button[contains(.,"Search")]').click()

        time.sleep(2)

        driver.find_element(By.XPATH, '//span[@class="mw-page-title-main"]')

        try:
            assert "Carpet" in driver.title
            print("Page has ", driver.title + " as Page title")
        except AssertionError:
            print("Title is different", driver.title)

        #Ardabil Carpet
        driver.find_element(By.XPATH, '(//img[@width="220"])[1]').click()

        time.sleep(2)

        try:
            assert "Ardabil Carpet" in driver.title
            print("Page has", driver.title + " as Page title")
            driver.get_screenshot_as_file('Carpet1.png')
        except AssertionError:
            print("Title is different", driver.title)

        time.sleep(2)
        driver.find_element(By.XPATH, "//button[@title='Close this tool (Esc)']").click()

        # Find 'Top' inner link before 'Azerbaijan' and click on it
        driver.find_element(By.ID, 'China').click()
        time.sleep(1)

        submit = driver.find_element(By.ID, "Azerbaijan")
        body = driver.find_element(By.CLASS_NAME, "reference")
        if submit:
            submit.click()
            print("Azerbaijan Carpet history")
        elif driver.body.send_keys(Keys.PAGE_DOWN):
            submit.click()

        time.sleep(2)

    #driver.quit()

    except NoSuchElementException:
        driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Some '
            'elements failed to load"}}')
    except Exception:
        driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Some '
            'exception occurred"}}')
    # Stop the driver
    driver.quit()

for cap in capabilities:
    Thread(target=run_session, args=(cap,)).start()