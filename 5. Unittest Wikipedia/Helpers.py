from pkg_resources import require
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.command import Command
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
import unittest
import requests
import time
#from faker import Faker
import random
from random import choice, randint



# Url for Website
WIKI_url = "https://www.wikipedia.org/"


# Asser driver title
def assert_title(driver, title):
    wait = WebDriverWait(driver, 10)
    wait.until(EC.title_is(title))
    assert title in driver.title
    print(f"Page has, {driver.title} as Page title")
    # Scr of page if pas has different title
    driver.get_screenshot_as_file(f"Page has different {title}.png")
    if not title in driver.title:
        raise Exception(f"Page {title} has wrong Title!")

# Delay
def delay1_3():
    time.sleep(random.randint(1, 3))

# API response Status code check
def check_API(driver):
    codeWiki = requests.get("https://www.wikipedia.org").status_code
    if codeWiki == 200:
        print("Wikipedia Url has correct", requests.get("https://www.wikipedia.org").status_code, " as status Code")
    else:
        print("Wikipedia Url has incorrect", requests.get("https://www.wikipedia.org").status_code,
                  "as status Code")

# Check that "Logo" is present and visible
def check_WebPage_Logo(driver):
    try:
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located((By.ID, 'www-wikipedia-org')))
        print(f"LOGO is present and correct!")
    except NoSuchElementException:
        print("Logo is NOT present on the Main Page")
        driver.get_screenshot_as_file("Page has different LOGO.png")

# Verify that "Русский", "Deutsch", "Italiano" is visible and clickable
def check_language_link(driver):
    try:
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located((By.ID, 'js-link-box-ru')))
        wait.until(EC.element_to_be_clickable((By.ID, 'js-link-box-ru')))
        wait.until(EC.visibility_of_element_located((By.ID, 'js-link-box-de')))
        wait.until(EC.element_to_be_clickable((By.ID, 'js-link-box-de')))
        wait.until(EC.visibility_of_element_located((By.ID, 'js-link-box-it')))
        wait.until(EC.element_to_be_clickable((By.ID, 'js-link-box-it')))
        print("Language links are visible and clickable")
    except NoSuchElementException:
        print("Language links doesn't work")

#Verify that the 'Search' filed is working appropriate
def check_Search_working(driver):
    try:
        driver.find_element(By.XPATH, '//body/div[1]')
        driver.find_element(By.ID, 'searchInput').click()
        driver.find_element(By.ID, 'searchInput').send_keys("Carpet")
        driver.find_element(By.XPATH, '//button[contains(.,"Search")]')
        time.sleep(2)
        driver.find_element(By.XPATH, '//button[contains(.,"Search")]').click()
        time.sleep(2)
        driver.find_element(By.XPATH, '//span[@class="mw-page-title-main"]')
        print("'Search' files working appropriate")
    except NoSuchElementException:
        print("'Search' files doesn't work")


#Verify that page has a correct name
def Verify_correct_title_on_the_page(driver):
    try:
        assert "Carpet" in driver.title
        print("Page has ", driver.title + " as Page title")
    except AssertionError:
        print("Title is different", driver.title)

#Assert 'Ardabil Carpet'
def assert_Ardabil_Carpet(driver):
    try:
        assert "Ardabil Carpet" in driver.title
        print("Page has", driver.title + " as Page title")
        driver.get_screenshot_as_file('Carpet1.png')
    except AssertionError:
        print("Title is different", driver.title)
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[@title='Close this tool (Esc)']").click()

# Find 'Top' inner link before 'Azerbaijan' and click on it
def verify_article_Azerbaijan(driver):
    driver.find_element(By.ID, 'China').click()
    time.sleep(1)
    submit = driver.find_element(By.ID, "Azerbaijan")
    body = driver.find_element(By.CLASS_NAME, "reference")
    if submit:
        submit.click()
        print("Main article 'Azerbaijani rug'")
    elif driver.body.send_keys(Keys.PAGE_DOWN):
        submit.click()
    time.sleep(2)


# Log-in function with correct username and correct password
def Log_in_func(driver):
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.ID, "pt-login-2")))
    wait.until(EC.element_to_be_clickable((By.ID, "pt-login-2")))
    driver.find_element(By.ID, "pt-login-2").click()
    assert 'Log in - Wikipedia' in driver.page_source
    try:
        wait.until(EC.visibility_of_element_located((By.ID, "wpLoginAttempt")))
        wait.until(EC.element_to_be_clickable((By.ID, "wpLoginAttempt")))
        # Click on Button
        driver.find_element(By.ID, "wpLoginAttempt").click()
        print("Log In Button is OK")
    except TimeoutException:
        print("Log In Button is NOT OK")
    time.sleep(2)
    # Verify that Placeholder for Username is visible and clickable
    wait.until(EC.visibility_of_element_located((By.ID, "wpName1")))
    wait.until(EC.element_to_be_clickable((By.ID, "wpName1")))
    # Clear Field
    driver.find_element(By.ID, "wpName1").clear()
    time.sleep(1)
    # Enter Username
    driver.find_element(By.ID, "wpName1").send_keys("LM2026")
    time.sleep(1)
    # Verify that Placeholder for Password is visible and clickable
    wait.until(EC.visibility_of_element_located((By.ID, "wpPassword1")))
    wait.until(EC.element_to_be_clickable((By.ID, "wpPassword1")))
    # Clear Field
    driver.find_element(By.ID, "wpPassword1").clear()
    time.sleep(1)
    # Enter Password
    driver.find_element(By.ID, "wpPassword1").send_keys("carpet123")
    time.sleep(2)
    # Verify Final Log In Visible and clickable
    wait.until(EC.visibility_of_element_located((By.ID, "wpLoginAttempt")))
    wait.until(EC.element_to_be_clickable((By.ID, "wpLoginAttempt")))
    # Click on The button "Log In"
    driver.find_element(By.ID, "wpLoginAttempt").click()

# Log-in function with correct username and valid password
def Log_in_func_with_wrong_password(driver):
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.ID, "pt-login-2")))
    wait.until(EC.element_to_be_clickable((By.ID, "pt-login-2")))
    driver.find_element(By.ID, "pt-login-2").click()
    assert 'Log in - Wikipedia' in driver.page_source
    # Button visible and clickable
    try:
        wait.until(EC.visibility_of_element_located((By.ID, "wpLoginAttempt")))
        wait.until(EC.element_to_be_clickable((By.ID, "wpLoginAttempt")))
        # Click on Button
        driver.find_element(By.ID, "wpLoginAttempt").click()
        print("Log In Button is OK")
    except TimeoutException:
        print("Log In Button is NOT OK")
    time.sleep(2)
    # Verify that Placeholder for Username is visible and clickable
    wait.until(EC.visibility_of_element_located((By.ID, "wpName1")))
    wait.until(EC.element_to_be_clickable((By.ID, "wpName1")))
    # Clear Field
    driver.find_element(By.ID, "wpName1").clear()
    time.sleep(1)
    # Enter Username
    driver.find_element(By.ID, "wpName1").send_keys("LM2026")
    time.sleep(1)
    # Verify that Placeholder for Password is visible and clickable
    wait.until(EC.visibility_of_element_located((By.ID, "wpPassword1")))
    wait.until(EC.element_to_be_clickable((By.ID, "wpPassword1")))
    # Clear Field
    driver.find_element(By.ID, "wpPassword1").clear()
    time.sleep(1)
    # Enter Password
    driver.find_element(By.ID, "wpPassword1").send_keys("1111111")
    time.sleep(2)
    # Verify Final Log In Visible and clickable
    wait.until(EC.visibility_of_element_located((By.ID, "wpLoginAttempt")))
    wait.until(EC.element_to_be_clickable((By.ID, "wpLoginAttempt")))
    # Click on The button "Log In"
    driver.find_element(By.ID, "wpLoginAttempt").click()

def Log_in_func_with_wrong_username(driver):
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.ID, "pt-login-2")))
    wait.until(EC.element_to_be_clickable((By.ID, "pt-login-2")))
    driver.find_element(By.ID, "pt-login-2").click()
    assert 'Log in - Wikipedia' in driver.page_source
    # Button visible and clickable
    try:
        wait.until(EC.visibility_of_element_located((By.ID, "wpLoginAttempt")))
        wait.until(EC.element_to_be_clickable((By.ID, "wpLoginAttempt")))
        # Click on Button
        driver.find_element(By.ID, "wpLoginAttempt").click()
        print("Log In Button is OK")
    except TimeoutException:
        print("Log In Button is NOT OK")
    time.sleep(2)
    # Verify that Placeholder for Username is visible and clickable
    wait.until(EC.visibility_of_element_located((By.ID, "wpName1")))
    wait.until(EC.element_to_be_clickable((By.ID, "wpName1")))
    # Clear Field
    driver.find_element(By.ID, "wpName1").clear()
    time.sleep(1)
    # Enter Username
    driver.find_element(By.ID, "wpName1").send_keys("Python")
    time.sleep(1)
    # Verify that Placeholder for Password is visible and clickable
    wait.until(EC.visibility_of_element_located((By.ID, "wpPassword1")))
    wait.until(EC.element_to_be_clickable((By.ID, "wpPassword1")))
    # Clear Field
    driver.find_element(By.ID, "wpPassword1").clear()
    time.sleep(1)
    # Enter Password
    driver.find_element(By.ID, "wpPassword1").send_keys("carpet123")
    time.sleep(2)
    # Verify Final Log In Visible and clickable
    wait.until(EC.visibility_of_element_located((By.ID, "wpLoginAttempt")))
    wait.until(EC.element_to_be_clickable((By.ID, "wpLoginAttempt")))
    # Click on The button "Log In"
    driver.find_element(By.ID, "wpLoginAttempt").click()

def Log_in_func_with_wrong_entrees(driver):
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.ID, "pt-login-2")))
    wait.until(EC.element_to_be_clickable((By.ID, "pt-login-2")))
    driver.find_element(By.ID, "pt-login-2").click()
    assert 'Log in - Wikipedia' in driver.page_source
    # Button visible and clickable
    try:
        wait.until(EC.visibility_of_element_located((By.ID, "wpLoginAttempt")))
        wait.until(EC.element_to_be_clickable((By.ID, "wpLoginAttempt")))
        # Click on Button
        driver.find_element(By.ID, "wpLoginAttempt").click()
        print("Log In Button is OK")
    except TimeoutException:
        print("Log In Button is NOT OK")
    time.sleep(2)
    # Verify that Placeholder for Username is visible and clickable
    wait.until(EC.visibility_of_element_located((By.ID, "wpName1")))
    wait.until(EC.element_to_be_clickable((By.ID, "wpName1")))
    # Clear Field
    driver.find_element(By.ID, "wpName1").clear()
    time.sleep(1)
    # Enter Username
    driver.find_element(By.ID, "wpName1").send_keys("Python")
    time.sleep(1)
    # Verify that Placeholder for Password is visible and clickable
    wait.until(EC.visibility_of_element_located((By.ID, "wpPassword1")))
    wait.until(EC.element_to_be_clickable((By.ID, "wpPassword1")))
    # Clear Field
    driver.find_element(By.ID, "wpPassword1").clear()
    time.sleep(1)
    # Enter Password
    driver.find_element(By.ID, "wpPassword1").send_keys("carpet123")
    time.sleep(2)
    # Verify Final Log In Visible and clickable
    wait.until(EC.visibility_of_element_located((By.ID, "wpLoginAttempt")))
    wait.until(EC.element_to_be_clickable((By.ID, "wpLoginAttempt")))
    # Click on The button "Log In"
    driver.find_element(By.ID, "wpLoginAttempt").click()

# Verify that driver.title has a correct name by another way
def Another_way_to_Verify_correct_title_on_the_page(driver):
    mainPageTitle = "Carpet - Wikipedia"
    if mainPageTitle == driver.title:
        print("Main Page Title is OK")
    else:
        print("Main Page Title is Different")
        driver.save_screenshot("WrongTitleOnTheMainPage.png")


# Click on "Create Account" link
def Sign_UP(driver):
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.ID, "pt-createaccount-2")))
    wait.until(EC.element_to_be_clickable((By.ID, "pt-createaccount-2")))
    driver.find_element(By.ID, "pt-createaccount-2").click()
    assert 'Create account - Wikipedia' in driver.page_source
    print("Page has ", driver.title + " as Page title")


# Create random account
def Create_random_account(driver):
    adjectives = ['afraid', 'brave', 'calm', 'fierce', 'kind', 'nice', 'proud', 'scary', 'witty', 'worried', 'split', 'help', 'steps']
    first_word = choice(adjectives)
    first_digit = str(randint(11, 199))
    user_name = first_word + first_digit
    password = randint(11111111, 99999999)
    print("New username is ", user_name)
    wait = WebDriverWait(driver, 10)
    driver.find_element(By.ID, "wpName2").click()
    driver.find_element(By.ID, "wpName2").send_keys(user_name)
    driver.find_element(By.ID, "wpPassword2").click()
    driver.find_element(By.ID, "wpPassword2").send_keys(password)
    driver.find_element(By.ID, "wpRetype").click()
    driver.find_element(By.ID, "wpRetype").send_keys(password)

# Create random account with password less than 8 characters
def Create_random_account_less_8(driver):
    adjectives = ['afraid', 'brave', 'calm', 'fierce', 'kind', 'nice', 'proud', 'scary', 'witty', 'worried', 'split', 'help', 'steps']
    first_word = choice(adjectives)
    first_digit = str(randint(11, 199))
    user_name = first_word + first_digit
    password = randint(11, 99999)
    print("New username is ", user_name)
    wait = WebDriverWait(driver, 10)
    driver.find_element(By.ID, "wpName2").click()
    driver.find_element(By.ID, "wpName2").send_keys(user_name)
    driver.find_element(By.ID, "wpPassword2").click()
    driver.find_element(By.ID, "wpPassword2").send_keys(password)
    driver.find_element(By.ID, "wpRetype").click()
    driver.find_element(By.ID, "wpRetype").send_keys(password)