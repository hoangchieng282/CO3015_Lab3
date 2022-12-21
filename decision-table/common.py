from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

def clickButton(driver,element,typ='xp',cp=1):
    try:
        if cp == 2:
            pass
        elif typ == "id":
            print("id")
            WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.ID, element))
                )
            # driver.implicitly_wait(10)
            driver.find_element(By.ID,element).click()
        elif typ == "al":
            print("link")
            WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, element))
                )
            # driver.implicitly_wait(10)
            driver.find_element(By.PARTIAL_LINK_TEXT, element).click()
        else:
            print("xpath")
            WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, element))
                )
            driver.find_element(By.XPATH,element).click()
    except:
        print("kiem ko ra: "+ str(cp))
        clickButton(driver,element,typ,2)

def login(driver,usrn,pssw):
    driver.get("https://sandbox.moodledemo.net")
    driver.find_element(By.XPATH, "/html/body/div[2]/nav/div[2]/div[5]/div/span").click()
    usrname = driver.find_element(By.ID,"username")
    usrname.clear()
    usrname.send_keys(usrn)

    pssword = driver.find_element(By.ID,"password")
    pssword.clear()
    pssword.send_keys(pssw)
    driver.find_element(By.ID,"loginbtn").click()

def setUp(driver):
    pass

def accessNoti(driver):
    driver.get("https://sandbox.moodledemo.net/message/notificationpreferences.php")

def disableGlobal(driver):
    # clickButton(driver,"/html/body/div[3]/div[3]/div/div[2]/div/section/div/div/div[2]/table/tbody/tr[2]/td[2]/form/div/div/label")

    WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.ID, "disable-notifications"))
                )
            # driver.implicitly_wait(10)
    driver.find_element(By.ID,"disable-notifications").click()
    time.sleep(3)

def disableNoti(driver):
    
    WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.ID, "disable-notifications"))
                )
            # driver.implicitly_wait(10)
    driver.find_element(By.ID,"message_provider_mod_assign_assign_notification_popup").click()

    
    
