import time
import random

from woniuboss2_ui.tools.service import Service


class Enterprise:

    def __init__(self, driver):
        self.driver = driver

    def click_add_button(self):
        self.driver.find_element_by_xpath('//div[@id="content"]/div[2]/div[1]/button').click()

    def input_add_newentname(self, newentname):
        u_newentname = self.driver.find_element_by_id('newentname')
        time.sleep(1)
        Service.send_input(u_newentname, newentname)

    def input_add_newentcate(self, newentcate):
        u_newentcate = self.driver.find_element_by_id('newentcate')
        Service.send_input(u_newentcate, newentcate)

    def input_add_newentaddr(self, newentaddr):
        u_newentaddre = self.driver.find_element_by_id('newentaddr')
        Service.send_input(u_newentaddre, newentaddr)

    def input_add_newentheade(self, newentheade):
        u_newentheade = self.driver.find_element_by_id('newentheader')
        Service.send_input(u_newentheade, newentheade)

    def input_add_newtel(self, newtel):
        u_newtel = self.driver.find_element_by_id('newtel')
        Service.send_input(u_newtel, newtel)

    def input_add_newemail(self, newemail):
        u_newemail = self.driver.find_element_by_id('newemail')
        Service.send_input(u_newemail, newemail)

    def input_add_neqq(self, neqq):
        u_neqq = self.driver.find_element_by_name('ent.qq')
        Service.send_input(u_neqq, neqq)

    def click_save_button(self):
        self.driver.find_element_by_css_selector('button.btn.btn-primary.btn-save').click()

    def windows_alert(self):
        Service.alert_windows(self.driver)

    def excute_add(self, contents):
        self.click_add_button()
        self.input_add_newentname(contents['newentname'])
        self.input_add_newentcate(contents['newentcate'])
        self.input_add_newentaddr(contents['newentaddr'])
        self.input_add_newentheade(contents['newentheade'])
        self.input_add_newtel(contents['newtel'])
        self.input_add_newemail(contents['newemail'])
        self.input_add_neqq(contents['neqq'])
        self.click_save_button()
        time.sleep(2)
        self.windows_alert()

    def click_edit_button(self):
        e_button = self.driver.find_element_by_xpath(
            '//table[@id="enterpriseTb"]/tbody/tr[%d]/td[7]/button' % random.randint(1, 3))
        e_button.click()
        time.sleep(2)

    def input_edit_newentname(self, newentname):
        u_newentname = self.driver.find_element_by_id('entName')
        time.sleep(1)
        Service.send_input(u_newentname, newentname)

    def input_edit_newentcate(self, newentcate):
        u_newentcate = self.driver.find_element_by_id('entCate')
        Service.send_input(u_newentcate, newentcate)

    def input_edit_newentaddr(self, newentaddr):
        u_newentaddre = self.driver.find_element_by_id('entAddr')
        Service.send_input(u_newentaddre, newentaddr)

    def input_edit_newentheade(self, newentheade):
        u_newentheade = self.driver.find_element_by_id('entHeader')
        Service.send_input(u_newentheade, newentheade)

    def input_edit_newtel(self, newtel):
        u_newtel = self.driver.find_element_by_id('entTel')
        Service.send_input(u_newtel, newtel)

    def input_edit_newemail(self, newemail):
        u_newemail = self.driver.find_element_by_id('entEmail')
        Service.send_input(u_newemail, newemail)

    def input_edit_neqq(self, neqq):
        u_neqq = self.driver.find_element_by_id('entQq')
        Service.send_input(u_neqq, neqq)

    def click_edit_save_button(self):
        self.driver.find_element_by_css_selector(
            'html body.modal-open div#company-modif.modal.in div.modal-dialog.modal-sm div.modal-content div.modal-footer button.btn.btn-primary.btn-save').click()

    def edit_windows_alert(self):
        Service.alert_windows(self.driver)

    def excute_edit(self, contents):
        self.click_edit_button()
        self.input_edit_newentname(contents['entName'])
        self.input_edit_newentcate(contents['entCate'])
        self.input_edit_newentaddr(contents['entAddr'])
        self.input_edit_newentheade(contents['entHeader'])
        self.input_edit_newtel(contents['entTel'])
        self.input_edit_newemail(contents['entEmail'])
        self.input_edit_neqq(contents['entQq'])
        time.sleep(2)
        self.click_edit_save_button()
        time.sleep(2)
        self.edit_windows_alert()

    def input_company_name(self, companyName):
        u_company = self.driver.find_element_by_name('companyName')
        Service.send_input(u_company, companyName)

    def click_query_button(self):
        self.driver.find_element_by_xpath('//div[@id="content"]/div[2]/div[1]/button[2]').click()

    def excute_query(self, companyName):
        self.input_company_name(companyName)
        self.click_query_button()
