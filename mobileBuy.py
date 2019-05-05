from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

username='13291261606'

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 5)
# 设置等待时间
url_login='https://m.damai.cn/damai/minilogin/index.html'
url_index='https://m.damai.cn/damai/home/index.html'

def login():
    driver.get(url_login)
    driver.switch_to.frame("alibaba-login-box")

    switchBtClass="password-login-link"
    userBoxID="fm-login-id"
    passwdBoxID="fm-login-password"


    switchBt=None
    while None == switchBt:
            switchBt = driver.find_element_by_class_name(switchBtClass)
    driver.execute_script("arguments[0].scrollIntoView();", switchBt)
    switchBt.click()

    userBox = None
    while None == userBox:
        userBox = driver.find_element_by_id(userBoxID)
    driver.execute_script("arguments[0].scrollIntoView();", userBox)
    userBox.send_keys(username)

    passwdBox = None
    while None == passwdBox:
        passwdBox = driver.find_element_by_id(passwdBoxID)
    driver.execute_script("arguments[0].scrollIntoView();", passwdBox)
    passwdBox.send_keys('dm9606!#')

    slideBarID='nc_2_n1z'
    slideBar = None
    while None == slideBar:
        slideBar = driver.find_element_by_id(slideBarID)
    action = ActionChains(driver)
    action.click_and_hold(slideBar).perform()
    action.reset_actions()
    action.move_by_offset(1000, 0).perform()

    submitClass='fm-submit'
    submitBt = None
    while None == submitBt:
        submitBt = driver.find_element_by_class_name(submitClass)
    driver.execute_script("arguments[0].scrollIntoView();", passwdBox)
    submitBt.click()

    driver.switch_to.default_content()


if __name__ == '__main__':
    # test()
    login()
    # main()