import asyncio
import os
import time
import traceback

from env import password, username
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from tcs import tcs, modal_title_selector


def login(driver):
    # Teachers and Students of HCMUT
    login_url = 'https://e-learning.hcmut.edu.vn/login/index.php?authCAS=CAS'
    driver.get(login_url)

    username_textbox = driver.find_element(by=By.ID, value="username")
    password_textbox = driver.find_element(by=By.ID, value="password")
    submit_button = driver.find_element(by=By.CLASS_NAME, value="btn-submit")

    username_textbox.send_keys(username)
    password_textbox.send_keys(password)
    submit_button.click()


def find_by_xpath_script(xpath):
    return f'return document.evaluate("{xpath}", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue'


def find_by_xpath(driver, xpath):
    script = find_by_xpath_script(xpath)
    elem = driver.execute_script(script)
    return elem


async def run_test_case(results, wait_for_element_timeout_secs, test_case):
    
    id = test_case.id
    name = test_case.name
    description = test_case.description
    step_1 = test_case.step_1
    step_2 = test_case.step_2
    step_3 = test_case.step_3

    print(f'START: {id} - {name} - {description}')

    try:
        # beforeEach
        driver = webdriver.Chrome()
        driver.maximize_window()

        login(driver)  # precondition
        WebDriverWait(driver, wait_for_element_timeout_secs).until(
            EC.url_changes('https://e-learning.hcmut.edu.vn'))

        # step 1
        driver.get(step_1.input.get('get'))
        (by, value), expected_text = step_1.output.get('ecs')[0]
        assert driver.find_element(by, value).text == expected_text

        # # step 2
        step_2_input = step_2.input
        step_2_output = step_2.output
        drag_drop_area_selector, upload_a_file_link_selector, choose_file_input_selector, x_file_path = step_2_input.get(
            'sequence')

        WebDriverWait(driver, wait_for_element_timeout_secs).until(
            EC.visibility_of_element_located(drag_drop_area_selector))
        find_by_xpath(driver, drag_drop_area_selector[1]).click()

        WebDriverWait(driver, wait_for_element_timeout_secs).until(
            EC.visibility_of_element_located(upload_a_file_link_selector))
        driver.find_element(*upload_a_file_link_selector).click()

        print(f'input: {os.path.basename(x_file_path)}')
        WebDriverWait(driver, wait_for_element_timeout_secs).until(
            EC.visibility_of_element_located(choose_file_input_selector)).send_keys(x_file_path)

        def file_exist_predicate(_driver): 
            try:
                elem = _driver.find_element(*choose_file_input_selector)
                return os.path.basename(x_file_path) in elem.get_attribute("value")
            except:
                return False

        WebDriverWait(driver, wait_for_element_timeout_secs, poll_frequency=1).until(file_exist_predicate)

        # step3
        step_3_input = step_3.input
        step_3_output = step_3.output

        sequence = step_3_input.get('sequence')
        ecs = step_3_output.get('ecs')
        upload_timeout = step_2_input.get('config').get('upload_timeout')
        for i, btn_selector in enumerate(sequence):
            WebDriverWait(driver, upload_timeout).until(
                EC.element_to_be_clickable(btn_selector))
            driver.find_element(*btn_selector).click()

            WebDriverWait(driver, upload_timeout).until(
                EC.all_of(*[EC.text_to_be_present_in_element(locator, text) for locator, text in [ecs[i]]]))

            if i != len(sequence) - 1:
                WebDriverWait(driver, upload_timeout).until(EC.invisibility_of_element_located(modal_title_selector))

        results.append(f'PASSED: {id} - {name} - {description}')

        driver.quit()
    except Exception as ex:
        results.append(f'FAILED: {id} - {name} - {description}')
        print(f'FAILED: {id} - {name} - {description}')
        print(ex)
        print(traceback.format_exc())


async def main():
    print(f"started at {time.strftime('%X')}")

    wait_for_element_timeout_secs = 60
    results = []
    tasks = []

    await asyncio.gather(*[run_test_case(
        results, wait_for_element_timeout_secs, test_case) for test_case in tcs])

    for result in results:
        print(result)

    print(f"finished at {time.strftime('%X')}")

if __name__ == '__main__':
    asyncio.run(main())
