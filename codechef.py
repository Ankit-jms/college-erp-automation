from urllib.request import urlopen
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

web= webdriver.Chrome(ChromeDriverManager().install())
from getpass import getpass
import time

# web.find_element_by_xpath("/html/body/form/div[3]/div/div[1]/div[1]/div/a/span[1]").click()

web.get("https://www.codechef.com/LRNDSA01/submit/TEST")
# web.find_element_by_xpath("//*[@id="ember351"]/div/div[1]/div[4]/div[1]/label").click()
with open ("",'r') as f:
    code=f.read()
code_element=web.find_element_by_id('edit-program')
code_element.send_keys(code)
web.find_element_by_xpath('//*[@id="ember351"]/div/div[1]/div[3]').click()
web.find_element_by_id("edit-submit").click()