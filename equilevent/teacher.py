from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from common import *

courseName = input("dai di man")

driver = webdriver.Chrome()
driver.get("https://sandbox.moodledemo.net/")
driver.maximize_window()

driver.implicitly_wait(5)
login(driver,"manager","sandbox")

# asd = "hehehe"
# WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.PARTIAL_LINK_TEXT,asd))
#     )


# driver.find_element(By.PARTIAL_LINK_TEXT,asd).click()
# WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID,"user-menu-toggle"))
#     )



# driver.find_element(By.ID,"user-menu-toggle").click()

# aaaa = "Log"
# WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.PARTIAL_LINK_TEXT,aaaa))
#     )

WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.PARTIAL_LINK_TEXT,courseName))
    )

driver.find_element(By.PARTIAL_LINK_TEXT,courseName).click()

    #Participants nav
clickButton(driver,"Participants","al")

    #Skip tour
try:
    driver.find_element(By.XPATH,"/html/body/span/div/div/div[4]/button[2]")
    clickButton(driver, "/html/body/span/div/div/div[4]/button[2]")
except:
    print("skip")

    #Enrol button
clickButton(driver,"/html/body/div[5]/div[5]/div/div[3]/div/section/div/div[1]/div/div[2]/div/div/form/div/input[1]")

time.sleep(5)
