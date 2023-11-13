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
import Helpers as H
from random import choice, randint
#from faker import Faker
import random




#fake = Faker()

class ChromeSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_1(self):
        driver = self.driver

        # Open Browser and go to Website
        driver.get(H.WIKI_url)
        print("______________________Positive_Test___________________________")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
              "Test 1 Verify that the Google search field can open the https://www.wikipedia.org page\n"
              "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

        H.delay1_3()
        # Check API Response Code
        H.check_API(driver)
        # Check Title is correct
        H.assert_title(driver, "Wikipedia")


        print("______________________Test is Passed!_____________________")

    def test_2(self):
            driver = self.driver
            wait = WebDriverWait(driver, 10)

            # Open Browser and go to Website
            driver.get(H.WIKI_url)
            print("______________________Positive_Test___________________________")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
                  "Test 2 Test 2 Verify that you open the https://www.wikipedia.org page and find the Page LOGO\n"
                  "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

            H.delay1_3()
            # Check API Response Code
            H.check_API(driver)
            # Check Title is correct
            H.assert_title(driver, "Wikipedia")
            # Check that "Logo" is present and visible
            H.check_WebPage_Logo(driver)


            print("______________________Test is Passed!_____________________")

    def test_3(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)

        # Open Browser and go to Website
        driver.get(H.WIKI_url)
        print("______________________Positive_Test___________________________")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
              "Test 3 Verify that language buttons is clickable and direct to correct page\n"
              "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

        H.delay1_3()
        # Check Title is correct
        H.assert_title(driver, "Wikipedia")
        # Check that "Logo" is present and visible
        H.check_WebPage_Logo(driver)
        # Verify that "Русский", "Deutsch", "Italiano" is visible and clickable
        H.check_language_link(driver)

        print("______________________Test is Passed!_____________________")

    def test_4(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)

        # Open Browser and go to Website
        driver.get(H.WIKI_url)
        print("______________________Positive_Test___________________________")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
                  "Test 4 Verify that the 'Search' filed is working appropriate\n"
                  "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        H.delay1_3()
        # Check Title is correct
        H.assert_title(driver, "Wikipedia")
        # Check that "Logo" is present and visible
        H.check_WebPage_Logo(driver)
        # Verify that the 'Search' filed is working appropriate
        H.check_Search_working(driver)

        print("______________________Test is Passed!_____________________")


    def test_5(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)

        # Open Browser and go to Website
        driver.get(H.WIKI_url)
        print("______________________Positive_Test___________________________")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
                  "Test 5 Validate the proper webpage has opened\n"
                  "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        H.delay1_3()
        # Check Title is correct
        H.assert_title(driver, "Wikipedia")
        # Check that "Logo" is present and visible
        H.check_WebPage_Logo(driver)
        # Verify that the 'Search' filed is working appropriate
        H.check_Search_working(driver)
        # Verify that driver.title has a correct name
        H.Verify_correct_title_on_the_page(driver)

        # Verify that page have "Ardabil Carpet" picture
        driver.find_element(By.XPATH, '(//img[@width="220"])[1]').click()
        time.sleep(2)

        # Assert 'Ardabil Carpet'
        H.assert_Ardabil_Carpet(driver)

        # Find 'Top' inner link before 'Azerbaijan' and click on it
        H.verify_article_Azerbaijan(driver)

        print("______________________Test is Passed!_____________________")


    def test_6(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)

        # Open Browser and go to Website
        driver.get(H.WIKI_url)
        print("______________________Positive_Test___________________________")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
              "Test 6 Verify that registration is available for user with valid Email and password\n"
              "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        H.delay1_3()
        # Check Title is correct
        H.assert_title(driver, "Wikipedia")
        # Check that "Logo" is present and visible
        H.check_WebPage_Logo(driver)
        # Verify that the 'Search' filed is working appropriate
        H.check_Search_working(driver)
        # Verify that driver.title has a correct name
        H.Verify_correct_title_on_the_page(driver)
        # Verify that driver.title has a correct name by another way
        H.Another_way_to_Verify_correct_title_on_the_page(driver)
        # Click on "Create Account" link
        H.Sign_UP(driver)
        # Create random account
        H.Create_random_account(driver)

        # Verify That button Sign up is visible and clickable
        wait.until(EC.visibility_of_element_located((By.ID, "wpCreateaccount")))
        wait.until(EC.element_to_be_clickable((By.ID, "wpCreateaccount")))

        time.sleep(10)

        wait = WebDriverWait(driver, 10)
        # Try to "Sign Up" With Existing Email !!! it has to be Error !
        # Error Captcha is required to verify that you're a human
        # Text "Captcha" Doesn't Allow to Sign Up
        try:
            driver.find_element(By.ID, "wpCreateaccount").click()
            print("At the moment, we CANNOT 'Sign Up' because the 'Captcha' is now allowing to complete the form ")
        except NoSuchElementException:
            print("Button 'Sign Up' Doesn't work")

        print("______________________Test is Passed!_____________________")

        time.sleep(2)

    def test_7(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)

        # Open Browser and go to Website
        driver.get(H.WIKI_url)
        print("______________________Positive_Test___________________________")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
                  "Test 7 Verify that user succesfull log in with valid Email and password\n"
                  "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

        H.delay1_3()
        # Check Title is correct
        H.assert_title(driver, "Wikipedia")
        # Check that "Logo" is present and visible
        H.check_WebPage_Logo(driver)
        # Verify that the 'Search' filed is working appropriate
        H.check_Search_working(driver)
        # Verify that driver.title has a correct name
        H.Verify_correct_title_on_the_page(driver)

        # "Log in" function
        H.Log_in_func(driver)

        # Verify that user got into the account and print text
        print('User got into Account:', driver.find_element(By.CLASS_NAME, "new").text)
        # Verify Main Page Logo is present
        print(driver.find_element(By.CLASS_NAME, "mw-logo-icon").get_attribute("src"))
        time.sleep(2)

        print("______________________Test is Passed!_____________________")

    def test_8(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)

        # Open Browser and go to Website
        driver.get(H.WIKI_url)
        print("______________________Negative Test___________________________")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
                  "Test 8 Verify that the user should be get the information about wrong of the password when he/she enter valid username and invalid password\n"
                  "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

        H.delay1_3()
        # Check Title is correct
        H.assert_title(driver, "Wikipedia")
        # Check that "Logo" is present and visible
        H.check_WebPage_Logo(driver)
        # Verify that the 'Search' filed is working appropriate
        H.check_Search_working(driver)
        # Verify that driver.title has a correct name
        H.Verify_correct_title_on_the_page(driver)

        # "Log in" function with valid username and invalid password
        H.Log_in_func_with_wrong_password(driver)

        # Verify that the user should be get the information about wrong of the password when he/she enter valid username and invalid password
        print("We've got a message:", driver.find_element(By.CLASS_NAME, "cdx-message__content").text)

    def test_9(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)

        # Open Browser and go to Website
        driver.get(H.WIKI_url)
        print("______________________Negative Test___________________________")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
                  "Test 9 Verify that the user should be get the information about wrong of the password when he/she enter invalid username and valid password\n"
                  "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        H.delay1_3()
        # Check Title is correct
        H.assert_title(driver, "Wikipedia")
        # Check that "Logo" is present and visible
        H.check_WebPage_Logo(driver)
        # Verify that the 'Search' filed is working appropriate
        H.check_Search_working(driver)
        # Verify that driver.title has a correct name
        H.Verify_correct_title_on_the_page(driver)

        # "Log in" function with wrong username and valid password
        H.Log_in_func_with_wrong_username(driver)

        # Verify that the user should be get the information about wrong of the password when he/she enter valid username and invalid password
        print("We've got a message:", driver.find_element(By.CLASS_NAME, "cdx-message__content").text)

        time.sleep(2)

        print("______________________Test is Passed!_____________________")

    def test_10(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)

        # Open Browser and go to Website
        driver.get(H.WIKI_url)
        print("______________________Negative Test___________________________")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
              "Test 10 Verify that the user should be get the information about wrong of the password when he/she enter invalid username and invalid password\n"
              "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        H.delay1_3()
        # Check Title is correct
        H.assert_title(driver, "Wikipedia")
        # Check that "Logo" is present and visible
        H.check_WebPage_Logo(driver)
        # Verify that the 'Search' filed is working appropriate
        H.check_Search_working(driver)
        # Verify that driver.title has a correct name
        H.Verify_correct_title_on_the_page(driver)

        # "Log in" function with wrong username and wrong password
        H.Log_in_func_with_wrong_entrees(driver)

        # Verify that the user should be get the information about wrong of the password when he/she enter valid username and invalid password
        print("We've got a message:", driver.find_element(By.CLASS_NAME, "cdx-message__content").text)

        time.sleep(2)

        print("______________________Test is Passed!_____________________")

    def test_11(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)

        # Open Browser and go to Website
        driver.get(H.WIKI_url)
        print("______________________Negative Test___________________________")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
              "Test 11 Verify that the user can't create account password less than 8 characters\n"
              "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        H.delay1_3()
        # Check Title is correct
        H.assert_title(driver, "Wikipedia")
        # Check that "Logo" is present and visible
        H.check_WebPage_Logo(driver)
        # Verify that the 'Search' filed is working appropriate
        H.check_Search_working(driver)
        # Verify that driver.title has a correct name
        H.Verify_correct_title_on_the_page(driver)
        # Click on "Create Account" link
        H.Sign_UP(driver)
        # Create random account with password less than 8 characters
        H.Create_random_account_less_8(driver)

        time.sleep(3)

        # Verify that User couldn't create account with less at 8 characters password
        driver.find_element(By.XPATH, "//div[contains(text(),'Passwords must be at least 8 characters.')]")
        print("We've got a message:",
              driver.find_element(By.XPATH, "//div[contains(text(),'Passwords must be at least 8 characters.')]").text)

        time.sleep(2)

        print("______________________Test is Passed!_____________________")



    def tearDown(self):
            self.driver.quit()