from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


def get_driver():
    # Options to make browsing easier
    options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    options.add_argument('disable-infobars')
    options.add_argument('start-maximized')
    options.add_argument(
        'disable-dev-shm-usage')
    options.add_argument(
        'no-sandbox')
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_argument('disable-blink-features=AutomationControlled')

    driver = webdriver.Chrome(options=options)
    driver.get('https://automated.pythonanywhere.com/login/')
    return driver


def main():
    driver = get_driver()
    sleep(2)
    driver.find_element(by='id', value='id_username').send_keys('automated')
    sleep(2)
    driver.find_element(by='id', value='id_password').send_keys('automatedautomated' + Keys.RETURN)
    sleep(2)
    driver.find_element(by='xpath', value='/html/body/nav/div/a').click()
    sleep(2)
    element = driver.find_element(by='xpath', value='/html/body/div[1]/div/h1[2]/div')
    element = element.text
    return element


def clean_text(element):
    element = element.split(': ')[1]
    return element


print(clean_text(main()))
