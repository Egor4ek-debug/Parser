import time
import keyboard
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
while(True):

    options = webdriver.ChromeOptions()

    options.add_argument(
        'user-agent = Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36')
    driver = webdriver.Chrome(executable_path='chromedriver/chromedriver.exe')

    try:
        driver.get('https://www.nngasu.ru/cdb/schedule/student.php?login=yes')
        time.sleep(2)
        gr_input = driver.find_element_by_name('USER_LOGIN')
        gr_input.clear()
        gr_input.send_keys('gr_PIE19.19')
        gr_input = driver.find_element_by_name('USER_PASSWORD')
        gr_input.clear()
        gr_input.send_keys('s3y6ea')
        login_button = driver.find_element_by_name('Login').click()
        time.sleep(2)
        # link = driver.find_elements_by_tag_name('a')[0].click()
        key = driver.find_element_by_id('diploma-iframe')
        # print(key.get_attribute('src'))
        driver.get(key.get_attribute('src'))
        link = driver.find_elements_by_tag_name('a')[1].get_attribute('href')


        time.sleep(2)
        driver.get(link)

        time.sleep(2)
        sendKeys = driver.find_element_by_class_name('mbTuDeF1')

        # sendCookies = driver.find_element_by_id('onetrust-accept-btn-handler')
        # sendCookies.click()
        keyboard.send('left')
        keyboard.send('enter')
        time.sleep(5)
        sendKeys.click()
        keyboard.send('enter')
        time.sleep(5)

        # get alert text

    except Exception as ex:
        print(ex)
# get alert text

# accept the alert
    finally:
        driver.close()
        driver.quit()
