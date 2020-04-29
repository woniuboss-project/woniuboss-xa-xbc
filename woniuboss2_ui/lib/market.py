import time

from woniuboss2_ui.tools.service import Service


class Market:

    def __init__(self, driver):
        self.driver = driver

    def click_decode_button(self):
        self.driver.find_element_by_id('btn-decrypt').click()
        time.sleep(2)

    def input_decode_passwd(self, decode_passwd):
        d_passwd = self.driver.find_element_by_name('secondPass')
        Service.send_input(d_passwd, decode_passwd)

    def click_decode(self):
        self.driver.find_element_by_css_selector(
            'div#secondPass-modal>div:first-child>div:first-child>div:nth-child(3)>button').click()

    # 解密流程
    def excute_decode(self, decode_passwd):
        self.click_decode_button()
        self.input_decode_passwd(decode_passwd)
        self.click_decode()

    def click_add_button(self):
        self.driver.find_element_by_xpath('//div[@id="queryDiv"]/button[2]').click()
        time.sleep(2)

    def region_select_random(self):
        selector = self.driver.find_element_by_name('cus.region')
        Service.select_random(selector)

    def depart_select_random(self):
        selector = self.driver.find_element_by_name('cus.department_id')
        Service.select_random(selector)

    def input_phone(self, phone):
        d_phone = self.driver.find_element_by_name('cus.tel')
        Service.send_input(d_phone, phone)

    def input_name(self, name):
        d_name = self.driver.find_element_by_name('cus.name')
        Service.send_input(d_name, name)

    def sex_select_random(self):
        selector = self.driver.find_element_by_name('cus.sex')
        Service.select_random(selector)

    def status_select_random(self):
        selector = self.driver.find_element_by_css_selector('select.text.form-control')
        Service.select_random(selector)

    def input_mail(self, mail):
        d_mail = self.driver.find_element_by_name('cus.email')
        Service.send_input(d_mail, mail)

    def input_QQ(self, QQ):
        d_qq = self.driver.find_element_by_name('cus.qq')
        Service.send_input(d_qq, QQ)

    def input_school(self, school):
        d_school = self.driver.find_element_by_name('cus.school')
        Service.send_input(d_school, school)

    def education_select_random(self):
        selector = self.driver.find_element_by_name('cus.education')
        Service.select_random(selector)

    def input_major(self, major):
        d_major = self.driver.find_element_by_name('cus.major')
        Service.send_input(d_major, major)

    def input_intent(self, intent):
        d_intent = self.driver.find_element_by_name('cus.intent')
        Service.send_input(d_intent, intent)

    def workage_select_random(self):
        selector = self.driver.find_element_by_name('cus.workage')
        Service.select_random(selector)

    def input_salary(self, salary):
        d_salary = self.driver.find_element_by_name('cus.salary')
        Service.send_input(d_salary, salary)

    def source_select_random(self):
        selector = self.driver.find_element_by_name('cus.source')
        Service.select_random(selector)

    def input_applposition(self, applposition):
        d_applposition = self.driver.find_element_by_name('cus.applposition')
        Service.send_input(d_applposition, applposition)

    def input_age(self, age):
        d_age = self.driver.find_element_by_name('cus.age')
        Service.send_input(d_age, age)

    def input_eduexp(self, eduexp):
        d_eduexp = self.driver.find_element_by_name('cus.eduexp')
        Service.send_input(d_eduexp, eduexp)

    def input_experience(self, experience):
        d_experience = self.driver.find_element_by_name('cus.experience')
        Service.send_input(d_experience, experience)

    def input_last_tracking_remark(self, last_tracking_remark):
        d_last_tracking_remark = self.driver.find_element_by_name('cus.last_tracking_remark')
        Service.send_input(d_last_tracking_remark, last_tracking_remark)

    def click_save_button(self):
        self.driver.find_element_by_id('addCusBtn').click()

    # 新增流程
    def excute_add_case(self, contents):
        self.excute_decode(contents['vp'])
        self.click_add_button()
        self.region_select_random()
        self.depart_select_random()
        self.input_phone(contents['phone'])
        self.input_name(contents['name'])
        self.sex_select_random()
        self.status_select_random()
        self.input_mail(contents['mail'])
        self.input_QQ(contents['qq'])
        self.input_school(contents['study'])
        self.education_select_random()
        self.input_major(contents['major'])
        self.input_intent(contents['want'])
        self.workage_select_random()
        self.input_salary(contents['money'])
        self.source_select_random()
        self.input_applposition(contents['test'])
        self.input_age(contents['age'])
        self.input_eduexp(contents['school'])
        self.input_experience(contents['job'])
        self.input_last_tracking_remark(contents['fllow'])
        self.click_save_button()

    def click_upload_button(self):
        self.driver.find_element_by_xpath('//div[@id="queryDiv"]/button[4]').click()

    def r_selector_random(self):
        selector = self.driver.find_element_by_id('regionSelect')
        Service.select_random(selector)

    def p_selector_random(self):
        selector = self.driver.find_element_by_id('dpetSelect')
        Service.select_random(selector)

    def upload_text(self, path):
        self.driver.find_element_by_id('files').send_keys(path)

    def uplodd_save_button(self):
        self.driver.find_element_by_xpath('//div[@id="upRes-modal"]/div[1]/div[1]/div[3]/button').click()

    # 上传文件
    def excute_upload(self, path):
        self.click_upload_button()
        self.r_selector_random()
        self.p_selector_random()
        self.upload_text(path)
        self.uplodd_save_button()

    def click_read_button(self):
        self.driver.find_element_by_xpath('//div[@id="queryDiv"]/button[3]').click()

    def click_ok_button(self):
        self.driver.find_element_by_xpath('/html/body/div[8]/div/div/div[3]/button[2]').click()

    # 读取邮件
    def excute_read_mail(self):
        self.click_read_button()
        self.click_ok_button()

    def ren_selector_random(self):
        selector = self.driver.find_element_by_name('regionSelect')
        Service.select_random(selector)

    def pal_selector_random(self):
        selector = self.driver.find_element_by_name('cus.last_status')
        Service.select_random(selector)

    def click_start_date(self):
        s_date = self.driver.find_element_by_name('s_time')
        s_date.click()

    def click_end_date(self):
        e_date = self.driver.find_element_by_name('e_time')
        e_date.click()

    def click_query_button(self):
        self.driver.find_element_by_xpath('//div[@id="queryDiv"]/button[1]').click()
        time.sleep(2)

    # 查询功能
    def excute_query(self):
        self.ren_selector_random()
        self.pal_selector_random()
        self.click_query_button()
