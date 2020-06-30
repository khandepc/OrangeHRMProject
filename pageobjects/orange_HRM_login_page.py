from generic.base import Base
from generic.loggingbase import logger as log

id_user_name="txtUsername"
id_password="txtPassword"
id_login_button="btnLogin"
id_welcome_admin="welcome"
link_text_logout="Logout"
xpath_invalid_error_msg="//*[@id='spanMessage']"
expected_error1="Invalid credentials"
expected_error2="Username cannot be empty"

class OrangeHRM_login_page(Base):

    def get_user_name_input_box_element(self):
        return self.identify_element("id",id_user_name)

    def enter_user_name(self,user_name):
        element=self.get_user_name_input_box_element()
        self.perform_action_on_elements(element,"sendkeys",user_name)
        self.capture_screenshot("enter_user_name")
        log.info("enter_user_name")


    def get_password_input_box_element(self):
        return self.identify_element("id",id_password)
    def enter_password(self,password):
        element=self.get_password_input_box_element()
        self.perform_action_on_elements(element,"sendkeys",password)
        self.capture_screenshot("enter_password")
        log.info("password entered")

    def get_login_button_element(self):
        return self.identify_element("id",id_login_button)
    def click_on_login_button(self):
        element=self.get_login_button_element()
        self.perform_action_on_elements(element,"click")
        self.capture_screenshot("click_on_login_button")
        log.info("clicked on log in button")

    def get_welcome_admin_element(self):
        return self.identify_element("id",id_welcome_admin)
    def click_on_welcome_admin(self):
        element=self.get_welcome_admin_element()
        self.perform_action_on_elements(element,"click")
        self.capture_screenshot("click_on_welcome_admin")
        log.info("click_on_welcome_admin")

    def get_logout_link_element(self):
        return self.identify_element("linktext",link_text_logout)
    def click_on_logout_link(self):
        element=self.get_logout_link_element()
        self.perform_action_on_elements(element,"click")
        self.capture_screenshot("click_on_logout_link")
        log.info("click_on_logout_link")

    def get_error_msg_text_element(self):
        return self.identify_elements("xpath",xpath_invalid_error_msg)

    def actual_error_msg(self):
        return_value=""
        list_of_error_msgs_element=self.get_error_msg_text_element()
        for error_text in list_of_error_msgs_element:
            return_value=self.perform_action_on_elements(error_text,"gettext")
        return return_value

    def assert_implement(self,expected_error_message):
        log.info("verifying actual error msg with expected error msg")
        assert self.actual_error_msg==expected_error_message
