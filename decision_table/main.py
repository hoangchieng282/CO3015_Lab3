
from common import *
from tc import *

def main():
    driver = webdriver.Chrome()
    driver.get("https://sandbox.moodledemo.net/")
    driver.maximize_window()
    
    login(driver,"student","sandbox")
    
    accessNoti(driver)

    # disableNoti(driver)

    # disableGlobal(driver)
    # time.sleep(4)
    test(driver)

def test(driver):
    for item in data:

        if item['globalNotification']==True:
            disableGlobal(driver)
        if item['customNotification']==True:
            disableNoti(driver)

        clickButton(driver,"/html/body/div[2]/nav/div[2]/div[3]/div[1]")
        ele = driver.find_element(By.XPATH,"/html/body/div[2]/nav/div[2]/div[3]/div[2]/div[2]/div/div[2]")
        notifi = 0
        if ele is not None:       
            notifi = 1
        try:        
            assert notifi == item['expected']
            print("Pass testcase: "+ item['id'] +": "+item['description'])
        except:
            print("Fail testcase: "+ item['id']+item['description'])

if __name__ == '__main__':
    main()