from selenium import webdriver

class LoginPage:
    button_start_login_link_text = "Login"
    textbox_username_xpath = "//*[@id='email']"
    textbox_password_xpath = "//*[@id='pwd']"
    button_login_xpath = "/html/body/app-root/app-login/section/div/div/div[2]/div/div/form/button"
    button_logout_link_text = "Log out"

    def __init__(self, driver):
        self.driver = driver

    def setStartlogin(self):
        self.driver.find_element_by_link_text(self.button_start_login_link_text).click()

    def setusername(self, username):
        self.driver.find_element_by_xpath(self.textbox_username_xpath).clear()
        self.driver.find_element_by_xpath(self.textbox_username_xpath).send_keys(username)

    def setpassword(self, password):
        self.driver.find_element_by_xpath(self.textbox_password_xpath).clear()
        self.driver.find_element_by_xpath(self.textbox_password_xpath).send_keys(password)

    def clicklogin(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()

    def clicklogout(self):
        self.driver.find_element_by_link_text(self.button_logout_link_text).click()
