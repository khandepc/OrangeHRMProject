from selenium import webdriver
from generic.seleniumbase import SeleniumBase
driver=webdriver.Chrome(executable_path="./drivers/chromedriver.exe")
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.implicitly_wait(5)

print(driver.title)

id_user_name="txtUsername"
id_password="txtPassword"
id_login_button="btnLogin"
id_welcome_admin="welcome"
link_text_logout="Logout"
xpath_invalid_error_msg="//*[@id='spanMessage']"
expected_error1="Invalid credentials"
expected_error2="Username cannot be empty"
expected_text="Username cannot be empty"

click_on_login_button=driver.find_element_by_id(id_login_button).click()
actual_text=driver.find_element_by_xpath(xpath_invalid_error_msg).text
print(actual_text)
assert actual_text==expected_text
print("actual error msg matching with expected msg")
print("test complete")
driver.close()