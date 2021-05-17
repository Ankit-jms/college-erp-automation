from urllib.request import urlopen
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

web= webdriver.Chrome(ChromeDriverManager().install())
# uri="https://www.wikipedia.org/" 
# data=urlopen(uri)
# # print(type(data))
# andriod_html=data.read()
# # print(andriod_html)
# # parsing data
# from bs4 import BeautifulSoup as soup 
# andriod_soup= soup(andriod_html,"html.parser")
# # print(andriod_soup)
# c=andriod_soup.findAll('h1',{})
# # print(c)
# d=andriod_soup("table",{ })
# import cv2
# img=cv2.imread('IMG_20191116_004909.JPG')
# from matplotlib import pyplot as plt 
# plt.imshow(img)
# plt.show()
from getpass import getpass
import time
# web=webdriver.Chrome("chromedriver.exe")

 web.find_element_by_xpath("/html/body/form/div[3]/div/div[1]/div[1]/div/a/span[1]").click()
web.get("https://www.codechef.com/LRNDSA01/submit/TEST")
# web.find_element_by_xpath("//*[@id="ember351"]/div/div[1]/div[4]/div[1]/label").click()
with open ("",'r') as f:
    code=f.read()
code_element=web.find_element_by_id('edit-program')
code_element.send_keys(code)
web.find_element_by_xpath('//*[@id="ember351"]/div/div[1]/div[3]').click()
web.find_element_by_id("edit-submit").click()
 
