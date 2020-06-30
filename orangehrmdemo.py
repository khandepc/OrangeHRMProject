from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from selenium.webdriver import Ie
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert


driver=Chrome(executable_path="./drivers/chromedriver.exe")
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/")
xpath_user_name_input_box="//div[@id='divUsername']/input[@id='txtUsername']"
xpath_password_input_box="//div[@id='divPassword']/input[@id='txtPassword']"
xpath_login_button="//div/*[@id='btnLogin']"
xpath_error_msg="//*[@id='spanMessage']"

expected_error_msg="Username cannot be empty"
driver.find_element_by_xpath(xpath_login_button).click()
actual_error=driver.find_elements_by_xpath(xpath_error_msg)
actual_error_text=""
for i in actual_error:
    actual_error_text=i.text

assert actual_error_text==expected_error_msg
driver.close()
