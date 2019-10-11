
	

#!/usr/bin/python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import requests
from time import sleep
import selenium


url = 'https://codewithmosh.com/sign_in'
lecture_index = 22

def main(lecture_index=0):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--start-maximized')
    browser = webdriver.Chrome(chrome_options=chrome_options)
    browser.implicitly_wait(10)
    browser.get(url)
    user_email = browser.find_element_by_id('user_email')
    user_email.send_keys('guga.rukhadze@mygps.ge')
    user_password = browser.find_element_by_id('user_password')
    user_password.send_keys('gugagurami123321')
    user_password.submit()
    course_button = browser.find_element_by_link_text('Courses')
    course_button.click()
    sleep(2.5)
    course_box = browser.find_elements_by_xpath(
        "//div[@class='course-listing-title']")

    # print(course_box[5].text) #react
    # exit()
    course_box[lecture_index].click()
    each_video = browser.find_elements_by_xpath(
        "//span[@class='lecture-name']")

    dl_links = []

    for i in range(0,len(each_video)):
        each_lecture = browser.find_elements_by_xpath(
            "//span[@class='lecture-name']")
        each_lecture[i].click()
        try:
            lecture_link = browser.find_element_by_class_name('download').get_attribute('href')  # working
            dl_links.append(lecture_link)
        except Exception as exc:
            print(exc)
            print('Exception Occured')
            continue
        back_button = browser.find_element_by_class_name("fa-angle-left")
        back_button.click()
        sleep(0.1)
    return dl_links


with open('links.txt', 'w') as link_file:
    link_file.write('\n'.join(main(lecture_index)))

