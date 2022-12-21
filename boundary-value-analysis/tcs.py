import os

from env import password, username
from selenium.webdriver.common.by import By

folder = os.path.dirname(os.path.abspath(__file__))
x_min_minus_1_path = f'{folder}/fixtures/0B.txt'
x_min_path = f'{folder}/fixtures/1B.txt'
x_min_plus_1_path = f'{folder}/fixtures/2B.txt'

x_normal_path = f'{folder}/fixtures/1MB.txt'

x_max_minus_1_path = f'{folder}/fixtures/500MiB-1B.txt'
x_max_path = f'{folder}/fixtures/500MiB.txt'
x_max_plus_1_path = f'{folder}/fixtures/500MiB+1B.txt'


class Step:
    def __init__(self, _input, output):
        self.input = _input
        self.output = output


class TestCase:
    def __init__(self, id: str, name: str, description: str, step_1: Step, step_2: Step, step_3: Step):
        self.id = id
        self.name = name
        self.description = description
        self.step_1 = step_1
        self.step_2 = step_2
        self.step_3 = step_3


common_step_1 = Step(
    {'get': 'https://e-learning.hcmut.edu.vn/user/files.php?lang=en'},
    {'ecs': [((By.XPATH, '/html/body/div[2]/div[4]/div/div[2]/div/section/div/h2'), 'Private files')]})

save_changes_button_selector = (
    By.XPATH, '/html/body/div[2]/div[4]/div/div[2]/div/section/div/div/div/form/div[3]/div[2]/fieldset/div/div[1]/span/input')

drag_drop_area_selector = (By.XPATH, "//a[@title='Add...']")

upload_a_file_link_selector = (By.XPATH, "//a[contains(.,'Upload a file')]")

choose_file_input_selector = (By.NAME, 'repo_upload_file')

error_modal_selector = (By.XPATH, '/html/body/div[10]/div[3]/div')

upload_this_file_button_selector = (
    By.XPATH, "//button[contains(., 'Upload this file')]")

file_list_div_selector = (By.CLASS_NAME, 'fp-content')

modal_title_selector = (
    By.XPATH, "//h3[contains(., 'File picker')]")

save_changes_button_selector = (By.NAME, 'submitbutton')

tcs = [
    TestCase('TC-001-001', 'x(min-1) = 0B', 'Can NOT upload:\n\t- 0B file',
             common_step_1,
             Step({
                 'sequence': [
                     drag_drop_area_selector,
                     upload_a_file_link_selector,
                     choose_file_input_selector,
                     x_min_minus_1_path,
                 ],
                 'config': {
                     'upload_timeout': 5
                 }
             }, {}),
             Step({
                 'sequence': [upload_this_file_button_selector]
             }, {
                 'ecs': [(
                     (By.CLASS_NAME, 'moodle-ajaxexception'),
                     "The file '0B.txt' is either empty or a folder. To upload folders zip them first."
                 )]
             })),

    TestCase('TC-002-001', 'x(min) = 1B', 'Can upload:\n\t- one 1B file',
             common_step_1,
             Step({
                 'sequence': [
                     drag_drop_area_selector,
                     upload_a_file_link_selector,
                     choose_file_input_selector,
                     x_min_path
                 ],
                 'config': {
                     'upload_timeout': 5
                 }
             }, {}),
             Step({
                 'sequence': [
                     upload_this_file_button_selector,
                     save_changes_button_selector
                 ]
             }, {
                 'ecs': [
                     (
                         file_list_div_selector,
                         os.path.basename(x_min_path)
                     ),
                     (
                         file_list_div_selector,
                         os.path.basename(x_min_path)
                     ),
                 ]
             })),

    TestCase('TC-003-001', 'x(min+1) = 2B', 'Can upload:\n\t- one 2B file',
             common_step_1,
             Step({
                 'sequence': [
                     drag_drop_area_selector,
                     upload_a_file_link_selector,
                     choose_file_input_selector,
                     x_min_plus_1_path
                 ],
                 'config': {
                     'upload_timeout': 5
                 }
             }, {}),
             Step({
                 'sequence': [
                     upload_this_file_button_selector,
                     save_changes_button_selector
                 ]
             }, {
                 'ecs': [
                     (
                         file_list_div_selector,
                         os.path.basename(x_min_plus_1_path)
                     ),
                     (
                         file_list_div_selector,
                         os.path.basename(x_min_plus_1_path)
                     ),
                 ]
             })),

    TestCase('TC-004-001', 'x(normal) = 1MB', 'Can upload:\n\t- one 1MB file',
             common_step_1,
             Step({
                 'sequence': [
                     drag_drop_area_selector,
                     upload_a_file_link_selector,
                     choose_file_input_selector,
                     x_normal_path
                 ],
                 'config': {
                     'upload_timeout': 5
                 }
             }, {}),
             Step({
                 'sequence': [
                     upload_this_file_button_selector,
                     save_changes_button_selector
                 ]
             }, {
                 'ecs': [
                     (
                         file_list_div_selector,
                         os.path.basename(x_normal_path)
                     ),
                     (
                         file_list_div_selector,
                         os.path.basename(x_normal_path)
                     ),
                 ]
             })),

    TestCase('TC-005-001', 'x(max-1) = 500MiB - 1B',
             'Can upload:\n\t- one (500MiB - 1B) file',
             common_step_1,
             Step({
                 'sequence': [
                     drag_drop_area_selector,
                     upload_a_file_link_selector,
                     choose_file_input_selector,
                     x_max_minus_1_path
                 ],
                 'config': {
                     'upload_timeout': 600
                 }
             }, {}),
             Step({
                 'sequence': [
                     upload_this_file_button_selector,
                     save_changes_button_selector
                 ]
             }, {
                 'ecs': [
                     (
                         file_list_div_selector,
                         os.path.basename(x_max_minus_1_path)
                     ),
                     (
                         file_list_div_selector,
                         os.path.basename(x_max_minus_1_path)
                     ),
                 ]
             })),

    TestCase('TC-006-001', 'x(max) = 500MiB',
             'Can upload:\n\t- one (500MiB) file',
             common_step_1,
             Step({
                 'sequence': [
                     drag_drop_area_selector,
                     upload_a_file_link_selector,
                     choose_file_input_selector,
                     x_max_path
                 ],
                 'config': {
                     'upload_timeout': 600
                 }
             }, {}),
             Step({
                 'sequence': [
                     upload_this_file_button_selector,
                     save_changes_button_selector
                 ]
             }, {
                 'ecs': [
                     (
                         file_list_div_selector,
                         os.path.basename(x_max_path)
                     ),
                     (
                         file_list_div_selector,
                         os.path.basename(x_max_path)
                     ),
                 ]
             })),

    TestCase('TC-007-001', 'x(max) = 500MiB + 1B',
             'Can NOT upload:\n\t- one (500MiB + 1B) file',
             common_step_1,
             Step({
                 'sequence': [
                     drag_drop_area_selector,
                     upload_a_file_link_selector,
                     choose_file_input_selector,
                     x_max_plus_1_path
                 ],
                 'config': {
                     'upload_timeout': 600
                 }
             }, {}),
             Step({
                 'sequence': [upload_this_file_button_selector]
             }, {
                 'ecs': [(
                     (By.CLASS_NAME, 'moodle-ajaxexception'),
                     "The file 500MiB+1B.txt is too large. The maximum size you can upload is 500MB."
                 )]
             })),
]
