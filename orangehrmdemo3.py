from pageobjects.orange_HRM_login_page import OrangeHRM_login_page
from generic.loggingbase import logger as log
import pytest


class Test1(OrangeHRM_login_page):
    @pytest.fixture()
    def setup(self):
        dd = self.read_config_file("base.ini", "section1")
        self.launch_browser(dd["browser"], dd["url"])
        log.info("application launch step 1 is done")
        yield
        self.close_application()

    def test_case_8(self,setup):
        self.click_on_login_button()
        log.info("clicked on login button step 2 is done")
        assert self.actual_error_msg() == "Username cannot be empty"
        log.info("asserting actual error text with expected error text")
