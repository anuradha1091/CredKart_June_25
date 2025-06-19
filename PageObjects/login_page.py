class Login_Page_Class:
    def __init__(self,driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element("id",
        "username").send_keys(username)
    def enter_password(selfself,password):
        selfself.driver.find_element("id",
        "password").send_keys(password)

    def click_login_button(self):
        self.driver.find_element("id",
        "loginBtn").click()