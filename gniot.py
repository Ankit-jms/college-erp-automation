from urllib.request import urlopen
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

web= webdriver.Chrome(ChromeDriverManager().install())
from getpass import getpass
import time
# web=webdriver.Chrome("chromedriver.exe")
web.get("http://gnioterp.com:155/login.aspx")
username_element=web.find_element_by_id("ctl00_CPLHome_txtuser")
username_element.send_keys("180606")
username_pass=web.find_element_by_id('ctl00_CPLHome_txtpassword')
username_pass.send_keys("20469")
web.find_element_by_id("ctl00_CPLHome_btnlogin").click()
time.sleep(10)
# web.find_element_by_xpath("/html/body/form/div[3]/div/div[1]/div[1]/div/a/span[1]").click()