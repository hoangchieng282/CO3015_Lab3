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
    # elif typ == "txt":
    #     # print(f'//button[text()=\"{element}\"]')
    #     WebDriverWait(driver, 10).until(
    #             EC.presence_of_element_located((By.XPATH, f'//button[text()=\"{element}\"]'))
    #         )

    #     driver.find_element(By.XPATH, '//button[text()="Dashboard"]').click()

def addText(driver,element,text,typ="id"):
    if typ == 'id':
        course_name = driver.find_element(By.ID,element)
    else:
        course_name = driver.find_element(By.XPATH,element)
    course_name.clear()
    course_name.send_keys(text)

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

def logout(driver): #todo
    clickButton(driver,"user-menu-toggle","id")
    print("logout")
    clickButton(driver,"Log","al")
    
def setMode(driver):
    clickButton(driver,"//input[@name='setmode']")
    try:
        WebDriverWait(driver,1).until(
                    EC.presence_of_element_located((By.XPATH, "/html/body/span/div/div/div[4]/button[2]"))
                )
        driver.find_element(By.XPATH,"/html/body/span/div/div/div[4]/button[2]").click()
    except:
        print("skip")


def addCourse(driver, courseName, shortName):
    login(driver,"manager","sandbox")
    #Edit button /html/body/div[5]/nav/div[2]/form/div/div/input
    clickButton(driver,"//input[@name='setmode']")
    #Add course
    # clickButton(driver,"/html/body/div[4]/div[4]/div/div[3]/div/section/div/div[3]/div/form/button")
    clickButton(driver,"//button[text()='Add a new course']")

    addText(driver,"id_fullname",courseName)

    addText(driver,"id_shortname",shortName)
    #Save and exit
    clickButton(driver,"/html/body/div[5]/div[4]/div/div[3]/div/section/div/form/div[3]/div[2]/fieldset/div/div[1]/span/input")
    driver.get("https://sandbox.moodledemo.net/")


    

def goToCourse(driver, courseName):
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT,courseName))
    )

    driver.find_element(By.PARTIAL_LINK_TEXT,courseName).click() 

def enrol2(driver):
    #Access course
    # clickButton(driver, "wtfman", "al")
    #Skip tour
    try:
        WebDriverWait(driver, 3).until(
                    EC.presence_of_element_located((By.XPATH, "/html/body/span/div/div/div[4]/button[2]"))
                )
        driver.find_element(By.XPATH,"/html/body/span/div/div/div[4]/button[2]").click()
    except:
        print("skip")

    clickButton(driver,"Participants","al")
    #Enrol button
    clickButton(driver,"/html/body/div[5]/div[5]/div/div[3]/div/section/div/div[1]/div/div[2]/div/div/form/div/input[1]")
    
    clickButton(driver,'//div[@id="fitem_id_userlist"]/div[@class="col-md-9 form-inline align-items-start felement"]/div[@class="d-md-inline-block mr-md-2 position-relative"]/span')
    # clickButton(driver,"/html/body/div[8]/div[2]/div/div/div[2]/form/fieldset/div[2]/div[1]/div[2]/ul/li[1]")
    time.sleep(1)
    clickButton(driver,"/html/body/div[8]/div[2]/div/div/div[2]/form/fieldset/div[2]/div[1]/div[2]/ul/li[1]")

    #Select teacher role
    clickButton(driver,"id_roletoassign","id")

    clickButton(driver,"/html/body/div[8]/div[2]/div/div/div[2]/form/fieldset/div[2]/div[2]/div[2]/select/option[2]")

    #Select Teri
    
    clickButton(driver,'//div[@id="fitem_id_userlist"]/div[@class="col-md-9 form-inline align-items-start felement"]/div[@class="d-md-inline-block mr-md-2 position-relative"]/span')
    # clickButton(driver,"/html/body/div[8]/div[2]/div/div/div[2]/form/fieldset/div[2]/div[1]/div[2]/ul/li[1]")
    time.sleep(1)
    clickButton(driver,"/html/body/div[8]/div[2]/div/div/div[2]/form/fieldset/div[2]/div[1]/div[2]/ul/li[2]")

    time.sleep(3)
    #ENrol
    clickButton(driver,"/html/body/div[8]/div[2]/div/div/div[3]/button[2]")

    try:
        WebDriverWait(driver, 3).until(
                    EC.presence_of_element_located((By.XPATH, "/html/body/span/div/div/div[4]/button[2]"))
                )
        driver.find_element(By.XPATH,"/html/body/span/div/div/div[4]/button[2]").click()
    except:
        print("skip")

    # clickButton(driver,"Participants","al")
    print("duoi")
    #Enrol button
    clickButton(driver,'//form[@id="enrolusersbutton-1"]/div/input[@type="submit"]')
    
    clickButton(driver,'//div[@id="fitem_id_userlist"]/div[@class="col-md-9 form-inline align-items-start felement"]/div[@class="d-md-inline-block mr-md-2 position-relative"]/span')
    # clickButton(driver,"/html/body/div[8]/div[2]/div/div/div[2]/form/fieldset/div[2]/div[1]/div[2]/ul/li[1]")
    time.sleep(1)
    clickButton(driver,"/html/body/div[8]/div[2]/div/div/div[2]/form/fieldset/div[2]/div[1]/div[2]/ul/li[1]")

    time.sleep(3)
    #ENrol
    clickButton(driver,"/html/body/div[8]/div[2]/div/div/div[3]/button[2]")

def addAssign(driver, courseName, assName):
    login(driver,"teacher","sandbox")

    #access course
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.PARTIAL_LINK_TEXT,courseName))
    )
    driver.find_element(By.PARTIAL_LINK_TEXT,courseName).click()
    # driver.refresh()

    #Skip tour
    try:
        WebDriverWait(driver, 3).until(
                    EC.element_to_be_clickable((By.XPATH, '/html/body/span/div/div/div[4]/button[2]'))
                )
        driver.find_element(By.XPATH,'/html/body/span/div/div/div[4]/button[2]').click()
        # clickButton(driver, "/html/body/span/div/div/div[4]/button[2]")
    except:
        print("skip")

    #Edit button /html/body/div[5]/nav/div[2]/form/div/div/input
    clickButton(driver,"//input[@name='setmode']")

    #Add activity
    # clickButton(driver,"/html/body/div[5]/div[5]/div/div[3]/div/section/div/div/div/ul/li[1]/div[2]/button")
    WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '//div[@id="coursecontentcollapse0"]/button/span[text()="Add an activity or resource"]'))
                )
    driver.find_element(By.XPATH,'//div[@id="coursecontentcollapse0"]/button/span[text()="Add an activity or resource"]').click()
    #Choose assignment
    # WebDriverWait(driver, 10).until(
    #                 EC.element_to_be_clickable((By.XPATH, "/html/body/div[9]/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div/a"))
    #             )
    # driver.find_element(By.XPATH,"/html/body/div[9]/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div/a").click()
    clickButton(driver,'//a[@title="Add a new Assignment"]')
    addText(driver,"id_name", assName)

    #Choose file number
    clickButton(driver,"/html/body/div[5]/div[5]/div/div[3]/div/section/div/form/fieldset[3]/div[2]/div[3]/div[2]/select/option[1]")

    #Choose file size
    clickButton(driver,"/html/body/div[5]/div[5]/div/div[3]/div/section/div/form/fieldset[3]/div[2]/div[4]/div[2]/select/option[6]")
    
    #Submit and return
    clickButton(driver,"id_submitbutton2","id")
    time.sleep(4)
intp = "equilivent-chih-testing"

