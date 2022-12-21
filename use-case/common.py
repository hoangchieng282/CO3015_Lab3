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
            
            WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.ID, element))
                )
            # driver.implicitly_wait(10)
            driver.find_element(By.ID,element).click()
        elif typ == "al":
            
            WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, element))
                )
            # driver.implicitly_wait(10)
            driver.find_element(By.PARTIAL_LINK_TEXT, element).click()
        else:
            
            WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, element))
                )
            driver.find_element(By.XPATH,element).click()
    except:
        # print("kiem ko ra: "+ str(cp))
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
    driver.get("https://sandbox.moodledemo.net/login/index.php")
    # driver.find_element(By.XPATH, "/html/body/div[2]/nav/div[2]/div[5]/div/span").click()
    usrname = driver.find_element(By.ID,"username")
    usrname.clear()
    usrname.send_keys(usrn)

    pssword = driver.find_element(By.ID,"password")
    pssword.clear()
    pssword.send_keys(pssw)
    driver.find_element(By.ID,"loginbtn").click()

def logout(driver): #todo
    clickButton(driver,"user-menu-toggle","id")
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

# intp = input("xin cai ten: ")
# intp2 = input("not cai nua di: ")

def testcase1(driver,courseName,item):
    login(driver,"manager","sandbox")
    #Edit button /html/body/div[5]/nav/div[2]/form/div/div/input
    clickButton(driver,"//input[@name='setmode']")
    #Add course
    # clickButton(driver,"/html/body/div[4]/div[4]/div/div[3]/div/section/div/div[3]/div/form/button")
    clickButton(driver,"//button[text()='Add a new course']")

    addText(driver,"id_fullname",courseName)

    addText(driver,"id_shortname",courseName)
    #Save and exit
    clickButton(driver,"/html/body/div[5]/div[4]/div/div[3]/div/section/div/form/div[3]/div[2]/fieldset/div/div[1]/span/input")
    try:
        assert driver.find_element(By.ID,"fitem_id_fullname") is not None
        print("Pass testcase: "+item['id']+" : "+item['description'])
    except:
        print("Fail testcase: "+item['id']+" : "+item['description'])
    logout(driver)
    

def testcase2(driver,courseName,item):
    login(driver,"manager","sandbox")
    #Edit button /html/body/div[5]/nav/div[2]/form/div/div/input
    clickButton(driver,"//input[@name='setmode']")
    #Add course
    # clickButton(driver,"/html/body/div[4]/div[4]/div/div[3]/div/section/div/div[3]/div/form/button")
    clickButton(driver,"//button[text()='Add a new course']")

    # addText(driver,"id_fullname",courseName)

    addText(driver,"id_shortname",courseName)
    #Save and exit
    clickButton(driver,"/html/body/div[5]/div[4]/div/div[3]/div/section/div/form/div[3]/div[2]/fieldset/div/div[1]/span/input")
    try:
        assert EC.visibility_of((By.ID,"id_error_fullname"))
        print("Pass testcase: "+item['id']+" : "+item['description'])
    except:
        print("Fail testcase: "+item['id']+" : "+item['description'])
    logout(driver)

def testcase3(driver,courseName,item):
    login(driver,"manager","sandbox")
    #Edit button /html/body/div[5]/nav/div[2]/form/div/div/input
    clickButton(driver,"//input[@name='setmode']")
    #Add course
    # clickButton(driver,"/html/body/div[4]/div[4]/div/div[3]/div/section/div/div[3]/div/form/button")
    clickButton(driver,"//button[text()='Add a new course']")

    addText(driver,"id_fullname",courseName)

    addText(driver,"id_shortname",courseName)

    clickButton(driver,"id_enddate_year","id")
    clickButton(driver,"//select[@id='id_enddate_year']/option[@value='2000']")
    #Save and exit
    clickButton(driver,"/html/body/div[5]/div[4]/div/div[3]/div/section/div/form/div[3]/div[2]/fieldset/div/div[1]/span/input")
    # id_error_enddate
    try:
        assert EC.visibility_of((By.ID,"id_error_enddate"))
        print("Pass testcase: "+item['id']+" : "+item['description'])
    except:
        print("Fail testcase: "+item['id']+" : "+item['description'])
    logout(driver)

