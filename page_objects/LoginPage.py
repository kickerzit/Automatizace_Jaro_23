from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    username_id = "user-name"
    password_id = "password"
    login_button_id = "login-button"
    page_title = "title"
    error_button_xpath = '//*[contains(@data-test, "error")]'

    def go_to_login_page(self):

        self.driver.get("https://www.saucedemo.com/")

    def input_username(self, username):

        self.driver.find_element(By.ID, self.username_id).clear()
        self.driver.find_element(By.ID, self.username_id).send_keys(username)
    
    def input_password(self, password):
        
        self.driver.find_element(By.ID, self.password_id).clear()
        self.driver.find_element(By.ID, self.password_id).send_keys(password)

    def click_on_login(self):

        self.driver.find_element(By.ID, self.login_button_id).click()

    def get_title_text(self):

        return self.driver.find_element(By.CLASS_NAME, self.page_title).text

    def get_error_message(self):
        
        return self.driver.find_element(By.XPATH, self.error_button_xpath).text