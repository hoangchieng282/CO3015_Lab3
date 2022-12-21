from common import *

driver = webdriver.Chrome()
driver.get("https://sandbox.moodledemo.net/")
driver.maximize_window()

driver.implicitly_wait(5)
WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/nav/div[2]/div[5]/div/span"))
    )


addAssign(driver,intp,intp2)