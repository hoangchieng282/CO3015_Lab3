
from common import *

driver = webdriver.Chrome()
driver.get("https://sandbox.moodledemo.net/")
driver.maximize_window()

driver.implicitly_wait(5)
WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/nav/div[2]/div[5]/div/span"))
    )

addCourse(driver,intp,intp)
goToCourse(driver,intp)
# enrol(driver)

goToCourse(driver,intp)
enrol2(driver)
logout(driver)

time.sleep(1)


# addAssign(driver,"Home")



print("done")
# driver.find_element(By.lable, "single_button63996a466b1fa10").click()
time.sleep(4)

driver.close()
