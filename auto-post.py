from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pyautogui
import random
import time

LOGIN_URL = 'https://www.facebook.com/login.php'


class FacebookLogin():
    def __init__(self, email, password, browser='Chrome'):
        #Store credentials for login   
        self.email = email
        self.password = password
        if browser == 'Chrome':
        #   Use chrome
            self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        elif browser == 'Firefox':
        #  Set it to Firefox
            self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        self.driver.get(LOGIN_URL)
        time.sleep(1) # Wait for some time to load


    def login(self):
        email_element = self.driver.find_element_by_id('email')
        email_element.send_keys(self.email) # Give keyboard input

        password_element = self.driver.find_element_by_id('pass')
        password_element.send_keys(self.password) # Give password as input too

        login_button = self.driver.find_element_by_id('loginbutton')
        login_button.click() # Send mouse click
        time.sleep(2) # Wait for 2 seconds for the page to show up

    def auto_scroll(self):
        t_end = time.time() + 30 * 1
        while time.time() < t_end:
            pyautogui.scroll(int(-30))

            pyautogui.time.sleep(int(3))

# if __name__ == '__main__':
# Enter your login cr.edentials here

#user_email = input("Enter your Facebook email: ")
#user_pass = input("Enter your Facebook password: ")


n=0
i=0
array=[]
# fb_login = FacebookLogin(email='reganrayner30@gmail.com', password='Kitmax2002', browser='Chrome')
fb_login = FacebookLogin(email='rcr.bis@yahoo.com', password='ob1canob', browser='Chrome')
fb_login.login()
fb_login.auto_scroll()
