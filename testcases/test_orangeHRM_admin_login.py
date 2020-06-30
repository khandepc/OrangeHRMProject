from pageobjects.orange_HRM_login_page import OrangeHRM_login_page
from generic.loggingbase import logger as log
import time
import pytest

class TestorangeHRMAdminLogin(OrangeHRM_login_page):

    # @pytest.fixture()
    # def set_up(self):
    #     dd = self.read_config_file("base.ini", "section1")
    #     self.launch_browser(dd["browser"], dd["url"])
    #     yield
    #     self.close_application()

    def test_001_orange_hrm_admin_login_with_valid_user_and_password(self):
        log.info("TC_001_test_orange_hrm_admin_login_with_valid_user_and_password")
        dd=self.read_config_file("base.ini","section1")
        self.launch_browser(dd["browser"],dd["url"])
        actual_title=self.get_page_details("title")
        expected_title="OrangeHRM"
        assert actual_title==expected_title,"is not equal to expected"
        self.enter_user_name("Admin")
        self.enter_password("admin123")
        self.click_on_login_button()
        self.capture_screenshot("test_orange_hrm_admin_login_with_valid_user_and_password")
        self.close_application()
    def test_002_orange_hrm_admin_login_with_valid_user_and_password_and_logout(self):
        log.info("TC_002_test_orange_hrm_admin_login_with_valid_user_and_password_and_logout")
        dd=self.read_config_file("base.ini","section1")
        self.launch_browser(dd["browser"],dd["url"])
        actual_title=self.get_page_details("title")
        expected_title="OrangeHRM"
        assert actual_title==expected_title,"is not equal to expected"
        self.enter_user_name("Admin")
        self.enter_password("admin123")
        self.click_on_login_button()
        self.click_on_welcome_admin()
        self.click_on_logout_link()
        self.capture_screenshot("test_orange_hrm_admin_login_with_invalid_user_name_and_valid_password")
        assert actual_title==expected_title, "is not equal to expected"
        self.close_application()
    def test_003_orange_hrm_admin_login_with_invalid_user_name_and_valid_password(self):
        log.info("TC_003_test_orange_hrm_admin_login_with_invalid_user_name_and_valid_password")
        dd=self.read_config_file("base.ini","section1")
        self.launch_browser(dd["browser"],dd["url"])
        actual_title=self.get_page_details("title")
        expected_title="OrangeHRM"
        assert actual_title==expected_title, "is not equal to expected"
        self.enter_user_name("00Admin")
        self.enter_password("admin123")
        self.click_on_login_button()
        self.capture_screenshot("test_orange_hrm_admin_login_with_invalid_user_name_and_valid_password")
        self.assert_implement("Invalid credentials")
        self.close_application()
    def test_004_orange_hrm_admin_login_with_valid_user_name_and_invalid_password(self):
        log.info("TC_004_test_orange_hrm_admin_login_with_valid_user_name_and_invalid_password")
        dd = self.read_config_file("base.ini", "section1")
        self.launch_browser(dd["browser"], dd["url"])
        actual_title = self.get_page_details("title")
        expected_title="OrangeHRM"
        assert actual_title==expected_title, "is not equal to expected"
        self.enter_user_name("Admin")
        self.enter_password("admin000")
        self.click_on_login_button()
        self.capture_screenshot("test_orange_hrm_admin_login_with_valid_user_name_and_invalid_password")
        self.assert_implement("Invalid credentials")
        self.close_application()
    def test_005_orange_hrm_admin_login_with_invalid_user_name_and_invalid_password(self):
        log.info("TC_005_test_orange_hrm_admin_login_with_invalid_user_name_and_invalid_password")
        dd = self.read_config_file("base.ini", "section1")
        self.launch_browser(dd["browser"], dd["url"])
        actual_title=self.get_page_details("title")
        expected_title="OrangeHRM"
        assert actual_title==expected_title, "is not equal to expected"
        self.enter_user_name("000Admin")
        self.enter_password("admin000")
        self.click_on_login_button()
        self.capture_screenshot("test_orange_hrm_admin_login_with_invalid_user_name_and_invalid_password")
        self.assert_implement("Invalid credentials")
        self.close_application()
    def test_006_orange_hrm_admin_login_without_user_name_and_valid_password(self):
        log.info("TC_006_test_orange_hrm_admin_login_without_user_name_and_valid_password")
        dd = self.read_config_file("base.ini", "section1")
        self.launch_browser(dd["browser"], dd["url"])
        actual_title=self.get_page_details("title")
        expected_title="OrangeHRM"
        assert actual_title==expected_title, "is not equal to expected"
        self.enter_password("admin123")
        self.click_on_login_button()
        self.capture_screenshot("test_orange_hrm_admin_login_without_user_name_and_valid_password")
        self.assert_implement("Username cannot be empty")
        self.close_application()
    def test_007_orange_hrm_admin_login_with_valid_user_name_and_without_password(self):
        log.info("TC_007_test_orange_hrm_admin_login_with_valid_user_name_and_without_password")
        dd = self.read_config_file("base.ini", "section1")
        self.launch_browser(dd["browser"], dd["url"])
        actual_title=self.get_page_details("title")
        expected_title="OrangeHRM"
        assert actual_title==expected_title, "is not equal to expected"
        self.enter_user_name("Admin")
        self.click_on_login_button()
        self.capture_screenshot("test_orange_hrm_admin_login_with_valid_user_name_and_without_password")
        self.assert_implement("Password cannot be empty")
        self.close_application()
    def test_008_orange_hrm_admin_login_without_user_name_and_without_password(self):
        log.info("TC_00_8_test_orange_hrm_admin_login_without_user_name_and_without_password")
        dd = self.read_config_file("base.ini", "section1")
        self.launch_browser(dd["browser"], dd["url"])
        actual_title=self.get_page_details("title")
        expected_title="OrangeHRM"
        assert actual_title==expected_title,"is not equal to expected"
        self.click_on_login_button()
        self.capture_screenshot("test_orange_hrm_admin_login_without_user_name_and_without_password")
        assert self.actual_error_msg=="Username cannot be empty"
        self.close_application()