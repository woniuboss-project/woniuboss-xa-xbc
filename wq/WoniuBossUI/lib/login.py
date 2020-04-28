from WoniuBossui.tools.service import Service


class Login:

    def __init__(self, driver):
        self.driver = driver

    # 输入用户名
    def input_username(self, username):
        u_name = self.driver.find_element_by_name('userName')
        Service.send_input(u_name, username)

    # 输入密码
    def input_password(self, password):
        u_pass = self.driver.find_element_by_name('userPass')
        Service.send_input(u_pass, password)

    # 输入验证码
    def input_checkcode(self, checkcode):
        u_code = self.driver.find_element_by_name("checkcode")
        Service.send_input(u_code, checkcode)

    # 点击登录按钮
    def click_login_button(self):
        self.driver.find_element_by_css_selector(".btn").click()

    # 登录功能实现
    def excute_login(self, contents):
        self.input_username(contents['username'])
        self.input_password(contents['password'])
        self.input_checkcode(contents['checkcode'])
        self.click_login_button()
