#!/usr/bin/python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import requests
from time import sleep
import selenium


url = 'https://codewithme.com/sign_in'


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--start-maximized')
browser = webdriver.Chrome(chrome_options=chrome_options)
browser.get(url)
user_email = browser.find_element_by_id('user_email')
user_email.send_keys('your_username@email.com')
user_password = browser.find_element_by_id('user_password')
user_password.send_keys('your_password')
user_password.submit()
course_button = browser.find_element_by_link_text('Courses')
course_button.click()

react_course = browser.find_elements_by_class_name('course-box-image')
react_course[4].click()
browser.implicitly_wait(5)
each_video = browser.find_elements_by_xpath(
    "//span[@class='lecture-name']")

dl_links = []

for i in range(7,len(each_video)):
    browser.implicitly_wait(30)
    each_lecture = browser.find_elements_by_xpath(
        "//span[@class='lecture-name']")
    each_lecture[i].click()
    try:
        lecture_link = browser.find_element_by_class_name('download').get_attribute('href')  # working
        dl_links.append(lecture_link)
    except Exception as exc:
        continue
    browser.implicitly_wait(20)
    back_button = browser.find_element_by_class_name("fa-angle-left")
    back_button.click()
    browser.implicitly_wait(20)
    sleep(0.1)


with open('links.txt', 'w') as link_file:
    link_file.write('\n'.join(dl_links))
