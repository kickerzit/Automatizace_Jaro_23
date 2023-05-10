from selenium.webdriver.common.by import By

class ProductPage:
    def __init__(self, driver):
        self.driver = driver

    page_title = "title"
    test_things_t_shirt_link_text = "Test.allTheThings() T-Shirt (Red)"
    t_shirt_desc_xpath =  "/html/body/div/div/div/div[2]/div/div/div[2]/div[2]"
    
    def get_title_text(self):
        
        return self.driver.find_element(By.CLASS_NAME, self.page_title).text

    def click_on_t_shirt(self):

        self.driver.find_element(By.LINK_TEXT, self.test_things_t_shirt_link_text).click()

    def get_t_shirt_description(self):

        return self.driver.find_element(By.XPATH, self.t_shirt_desc_xpath).text

    def click_add_to_cart(self):

        self.driver.find_element(By.ID, self.add_to_cart_button_id).click()

    def click_on_cart(self):

        self.driver.find_element(By.CLASS_NAME, self.cart_button_class).click()