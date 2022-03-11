from calendar import c
from ssl import DER_cert_to_PEM_cert
import time
from selenium import webdriver
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()

options.add_argument(
    'user-agent = Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36')
driver = webdriver.Chrome(executable_path='chromedriver/chromedriver.exe')
try:
    driver.get('https://www.nngasu.ru/cdb/schedule/student.php?login=yes')

    gr_input = driver.find_element_by_name('USER_LOGIN')
    gr_input.clear()
    gr_input.send_keys('gr_PIE19.19')
    gr_input = driver.find_element_by_name('USER_PASSWORD')
    gr_input.clear()
    gr_input.send_keys('s3y6ea')

    login_button = driver.find_element_by_name('Login').click()
    # link = driver.find_elements_by_tag_name('a')[0].click()
    key = driver.find_element_by_id('diploma-iframe')
    # print(key.get_attribute('src'))
    driver.get(key.get_attribute('src'))
    link = driver.find_elements_by_tag_name('a')[0].click()

    time.sleep(5)


except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
