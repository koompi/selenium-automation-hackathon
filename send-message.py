from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
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
    
    def send_message(self):
        # msg = self.driver.findElement(By.xpath(".//*[@id='u_0_h']/li[1]/div/a/span")).click();
        # msg = self.driver.find_element_by_name('Message')
        pass
    def go_url(self, user_id):
        url_go = "https://m.facebook.com/messages/read/?tid=cid.c.{}%3A100054040111270&entrypoint=jewel&refid=11#fua".format(user_id)
    
        self.driver.get(url_go)
        # msg = self.driver.find_elements('<div class="_7kpk"><div class="_kmc _7kpg navigationFocus" role="presentation"><div class=" _3oh-"><div tabindex="-1"><div class="_5rp7 _5rp8"><div class="_1p1t"><div class="_1p1v" id="placeholder-9cbe1" style="white-space: pre-wrap;">Type a message...</div></div><div class="_5rpb"><div aria-autocomplete="list" aria-controls="js_6" aria-describedby="js_0" aria-expanded="false" aria-label="Type a message..." class="notranslate _5rpu" contenteditable="true" role="combobox" spellcheck="true" tabindex="0" style="outline: none; user-select: text; white-space: pre-wrap; overflow-wrap: break-word;"><div data-contents="true"><div class="" data-block="true" data-editor="9cbe1" data-offset-key="8n56o-0-0"><div data-offset-key="8n56o-0-0" class="_1mf _1mj"><span data-offset-key="8n56o-0-0"><br data-text="true"></span></div></div></div></div></div></div></div><div class="_5ca7" id="js_0">Conversation with <span>Isaac Jackson Reay</span>. Updated Today by <span>You: <span>fk mennn</span></span></div></div></div><a aria-label="Choose an emoji" class="_30yy _7odb" role="button" title="Choose an emoji" data-testid="m4_emoji_button" href="#"><svg height="24px" width="24px" viewBox="0 0 26 26"><g fill="none" fill-rule="evenodd"><polygon points="0,26 26,26 26,0 0,0 "></polygon><path d="m19.1311,16.73095c-0.4325,-0.3545 -1.0775,-0.302 -1.441,0.122c-1.171,1.3615 -2.883,2.142 -4.697,2.142c-1.8135,0 -3.526,-0.7805 -4.697,-2.142c-0.363,-0.4225 -1.008,-0.4765 -1.441,-0.122c-0.432,0.355 -0.488,0.986 -0.1245,1.408c1.5605,1.8145 3.8435,2.855 6.2625,2.855c2.4195,0 4.702,-1.0405 6.2625,-2.855c0.3635,-0.422 0.3075,-1.053 -0.1245,-1.408m-2.1355,-7.731c-0.9375,0 -1.5,0.75 -1.5,2c0,1.25 0.5625,2 1.5,2c0.9375,0 1.5,-0.75 1.5,-2c0,-1.25 -0.5625,-2 -1.5,-2m-8,0c-0.9375,0 -1.5,0.75 -1.5,2c0,1.25 0.5625,2 1.5,2c0.9375,0 1.5,-0.75 1.5,-2c0,-1.25 -0.5625,-2 -1.5,-2m4.0045,16c-6.6275,0 -12,-5.3725 -12,-12c0,-6.6275 5.3725,-12 12,-12c6.6275,0 12,5.3725 12,12c0,6.6275 -5.3725,12 -12,12" fill="#0099ff"></path></g></svg></a></div>')
        msg = self.driver.find_element(By.ID, 'composerInput')
        msg.send_keys('''Subject: ប្រកាសការណែនាំពី KOOMPI E11

KOOMPI គឺជាគំនិតផ្តួចផ្តើមមួយដែលកើតចេញពីការដែល យើងយកកុំព្យូទ័រ យួរដៃដែលអាចកែច្នៃបានមកតម្លើងថ្មី និងប្រគល់បន្តទៅឲ្យសិស្សដែល ខ្វះខាត។ សព្វថ្ងៃ KOOMPI បានធ្វើប្រតិបត្តិការដោយផ្អែកលើគោលជំហរ ដ៍រឹងមាំ គឺបង្កើតឡើងដើម្បីក្លាយជាឧបករណ៍សំរាប់អ្នកច្នៃប្រឌិតជំនាន់ក្រោយ។

អ្វីគ្រប់យ៉ាងដែលយើងខិតខំធ្វើ  និងពាក្យសម្តីទាំងអស់ឆ្លុះបញ្ជាុំងពីពិភពដែល គ្មានដែនកំណត់នៃសមត្ថភាព សម្រាប់ការរៀនសូត្រដោយខ្លួនឯងតាមរយៈ ការលើកទឹកចិត្ត ការចង់ដឹងចង់ឃើញ ភាពបត់បែន និងការស្រមើលស្រមៃ បង្កើនភាពច្នៃប្រឌិត។

ចាប់ពីខែសីហាឆ្នាំ ២០២០ តទៅ យើងមានមោទនភាព ក្នុងការបង្ហាញនូវការ បង្កើតថ្មីបំផុតពីពួកយើង គឺ KOOMPI E11។  ដូចគ្នានឹង កុំព្យូទ័រម៉ូឌែលដំបូង របស់យើងដែលបានចេញលក់នៅឆ្នាំ ២០១៨ កន្លងមកគឺ KOOMPI E11 ដែល ដំណើរការលើប្រព័ន្ធប្រតិបត្តិការ KOOMPI OS ផ្អែកមូលដ្ឋានលើ Archlinux ។ បច្ចុប្បន្ន ឧបករណ៍នេះគឺត្រូវបានបើកជាផ្លូវការ សម្រាប់ការបញ្ជាទិញជាមុន ហើយនឹងត្រូវបានតម្លើងគ្រឿងបណ្គុំផ្ទាល់ដោយក្រុមបច្ចេកទេសរបស់យើង។

សូមចូលទៅកាន់គេហទំព័រ koompi.com សម្រាប់ពត៍មានបន្ថែមទៀត និងចូលរួមជាមួយសហគមន៍របស់យើងតាមរយះ t.me/koompi

សូមអរគុណ និងជូនពរសំណាងល្អ,

ដោយក្តីស្រលាញ់, KOOMPI''')
        send_button = self.driver.find_element(By.ID, 'u_0_8')
        send_button.click()
# if __name__ == '__main__':
# Enter your login cr.edentials here

user_email = input("Enter your Facebook email: ")
user_pass = input("Enter your Facebook password: ")


n=0
i=0
array=[]
# fb_login = FacebookLogin(email='reganrayner30@gmail.com', password='Kitmax2002', browser='Chrome')
fb_login = FacebookLogin(email=user_email, password=user_pass, browser='Chrome')
fb_login.login()

user_id = open('test.txt', 'r')
lines = user_id.readlines()
for line in lines:
    n=n+1
    array.append(line)
while i<n:
    fb_login.go_url(array[i])
    i=i+1
    time.sleep(random.randint(5,20))
    