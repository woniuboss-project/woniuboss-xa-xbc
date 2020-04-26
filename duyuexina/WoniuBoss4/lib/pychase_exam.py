import time
from selenium.webdriver.common.by import By

from WoniuBoss4.tools.service import Service


class PhaseExam:

    def __init__(self, driver):
        self.driver = driver
        Service.miss_login(driver,'../config/base.conf')

    def click_student_manage_link(self):
        self.driver.find_element_by_link_text('学员管理').click()

    def click_phase_exam_link(self):
        Service.wait_until_element_is_visible(self.driver, By.LINK_TEXT, '阶段考评')
        self.driver.find_element_by_link_text('阶段考评').click()

    def click_sigle_import_btn(self):
        Service.wait_until_element_is_visible(self.driver,By.CSS_SELECTOR,'#pe-result > tbody > tr:nth-child(1) >'
                                                                          ' td:nth-child(9) > button')
        self.driver.find_element_by_css_selector('#pe-result > tbody > tr:nth-child(1) > td:nth-child(9) > button').click()

    def select_class(self,class_name):
        Service.box_id_click(self.driver,'ph_cl',class_name)

    def input_score(self,score):
        ele = self.driver.find_element_by_css_selector('#phaseExam-form > div:nth-child(3) > div:nth-child(1) > input:nth-child(2)')
        Service.send_input(ele,score)

    def select_phase(self,phase):
        Service.box_id_click(self.driver,'ph_phase',phase)

    def input_comment(self,comment):
        ele = self.driver.find_element_by_css_selector('#phaseExam-form > div:nth-child(3) > '
                                                       'div:nth-child(3) > textarea')
        Service.send_input(ele,comment)

    def click_save_btn(self):
        self.driver.find_element_by_css_selector('#phaseExam-modal > div > div > div.modal-footer > button').click()

    def do_entry_sigle_phase_exam(self,class_name,score,phase,comment):
        self.click_student_manage_link()
        self.click_phase_exam_link()
        self.click_sigle_import_btn()
        self.select_class(class_name)
        self.input_score(score)
        self.select_phase(phase)
        self.input_comment(comment)
        self.click_save_btn()
        time.sleep(2)