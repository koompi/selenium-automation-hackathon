from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait
#browser = webdriver.Chrome()
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys



options = Options()
options.add_argument('--user-agent="Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1"')
options.add_argument('--window-size=375,812')
options.add_argument('user-data-dir=selenium')
browser = webdriver.Chrome(options=options)

browser.get("https://m.facebook.com/")



#username = browser.find_element_by_id("m_login_email")
#password = browser.find_element_by_id("pass")
#submit   = browser.find_element_by_id("loginbutton")

#username.send_keys("lionelsea@gmail.com")