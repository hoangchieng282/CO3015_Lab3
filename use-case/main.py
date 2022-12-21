
from common import *
from tc import *
driver = webdriver.Chrome()
driver.get("https://sandbox.moodledemo.net/")
driver.maximize_window()

driver.implicitly_wait(5)
WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/nav/div[2]/div[5]/div/span"))
    )

testcase1(driver,data[0]['id'],data[0])
testcase2(driver,data[1]['id'],data[1])
testcase3(driver,data[2]['id'],data[2])
# addCourse(driver,intp,intp)
# goToCourse(driver,intp)
# enrol(driver)

# goToCourse(driver,intp)
# enrol2(driver)
# logout(driver)


# addAssign(driver,"Home")



# print("done")
# # driver.find_element(By.lable, "single_button63996a466b1fa10").click()
# time.sleep(4)

driver.close()
