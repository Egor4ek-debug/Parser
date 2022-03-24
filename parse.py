import time
from matplotlib.pyplot import cla
from selenium import webdriver
from bs4 import BeautifulSoup


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
    time.sleep(5)
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    schedule = soup.find('tbody')
    # for links in schedule:
    #     link = driver.find_element_by_tag_name('a').get_attribute('href')
    #     print(link)
    with open('str_ru_text_1.txt', 'w', encoding='utf-8') as f:
        for i in schedule:
            names = driver.find_element_by_css_selector('#schedule-student-container > table > tbody > tr:nth-child(3) > td:nth-child(1)').text
            link = driver.find_element_by_tag_name('a').get_attribute('href')
            f.write(names)
            f.write('\t')
            f.write(link)
            f.write('\n')
        print('\t')
        f.close()

    # get alert text

except Exception as ex:
    print(ex)
# get alert text

# accept the alert
finally:
    driver.close()
    driver.quit()
