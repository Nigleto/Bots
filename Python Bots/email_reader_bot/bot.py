import time

from selenium import webdriver

from config import keys

import re

driver = webdriver.Chrome('./chromedriver')


def order(keys):
    driver.get(keys['destination'])

    driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[4]/ul[1]/li[2]').click()
    print('Directed to correct page...')
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys(keys["email"])
    print('Email entered...')
    driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/div[2]').click()
    print('Going to next page...')
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys(keys["password"])
    print('Entered password...')
    driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/div[2]').click()
    print('Going to next page...')
    time.sleep(2)
    inbox = driver.find_element_by_xpath("//*[contains(@title,'Unread')]").text

    pattern = re.compile("\w+\s+\((\d+)\)")
    match = re.search(pattern, inbox)
    if match:
        print("Total no of unread mails in your inbox are ", int(match.group(1)))


if __name__ == '__main__':
    order(keys)

input()
