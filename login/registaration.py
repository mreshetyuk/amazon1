from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from login.variables import user_name
from amazon1.login.variables import *
from login.web_driver import  driver
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException
import time as t


def registration():
    drv=driver()
    drv.get("https://www.amazon.com")
    #t.sleep(2)
    ActionChains(drv).move_to_element(drv.find_element_by_xpath("//*[@id='nav-link-accountList']/span[1]"))
    drv.find_element_by_xpath("//*[@id='nav-signin-tooltip']/div/a").click()
    drv.find_element_by_xpath("//*[@id='ap_customer_name']").send_keys(new_user_name())
    drv.find_element_by_xpath("//*[@id='ap_password']").send_keys(newUserPassword())
    drv.find_element_by_xpath("//*[@id='ap_password_check']").send_keys(newUserPassword())
    drv.find_element_by_xpath("//*[@id='continue']").click()
    drv.find_element_by_xpath("//*[@id='signInSubmit']").click()
    #drv.quit()

registration()
