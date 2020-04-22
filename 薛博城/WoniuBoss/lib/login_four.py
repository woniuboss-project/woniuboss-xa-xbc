from selenium.webdriver.support.select import Select
import time
from WoniuBoss.tools.service import Service

class Login:
    def __init__(self,driver):
        self.driver=driver

    #输入账号
    def input_name(self,username):
        uname=self.driver.find_element_by_name('userName')
        Service.send_input(uname,username)
    #输入密码
    def input_passwd(self,password):
        upass=self.driver.find_element_by_name('userPass')
        Service.send_input(upass,password)

    #输入验证码
    def input_verifycode(self,verifycode):
        vercode=self.driver.find_element_by_name('checkcode')
        Service.send_input(vercode,verifycode)

    #点击登录
    def click_button(self):
        self.driver.find_element_by_xpath('//button[@onclick="login();"]').click()

    #登录动作组合
    def do_login(self,path,account):
        Service.open_page(self.driver,path)
        self.input_name(account['uname'])
        self.input_passwd(account['upass'])
        self.input_verifycode(account['vcode'])
        self.click_button()