from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time as t

chrome_driver_path="C:\\Users\\Max\\Desktop\\python\\chromedriver.exe"
#driver = webdriver.Chrome("C:\\Users\\Max\\Desktop\\python\\chromedriver.exe")
driver = webdriver.Chrome(chrome_driver_path)
#driver.get("https://www.amazon.com/Motorola-Certified-Comcast-Spectrum-BrightHouse/dp/B01A1E6BA2/ref=pd_sim_147_1?_encoding=UTF8&pd_rd_i=B01A1E6BA2&pd_rd_r=KJWSG8QVJFK5ZKMTQC7G&pd_rd_w=UKfRh&pd_rd_wg=MMAxP&psc=1&refRID=KJWSG8QVJFK5ZKMTQC7G")




def getNewEmail():
    driver.get("https://www.mailinator.com/")
    t.sleep(10)
    driver.find_element_by_xpath("html/body/section[1]/div/div[3]/div[2]/div[2]/div[2]/h4[3]/span/a").click()
    t.sleep(20)
    email= driver.find_element_by_xpath("//*[@id='query_data']/div[4]").text
    return email


tex = getNewEmail()
print(tex)

#close_driver()


