from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver import FirefoxProfile
from selenium.webdriver import FirefoxOptions
from selenium.webdriver import IeOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from generic.loggingbase import logger as log

class SeleniumBase:

    def launch_browser(self,browser_name,url):
        global driver
        try:
            if browser_name=="chrome":
                chromeoptions=ChromeOptions()
                chromeoptions.add_argument("start-maximized")
                chromeoptions.add_argument("disable-notifications")
                chromeoptions.add_argument("--ignore-certificate-errors")
                chromeoptions.add_argument("--disable-infobars")
                chromeoptions.add_argument("--disable-extensions")
                driver=webdriver.Chrome(executable_path="./drivers/chromedriver.exe",options=chromeoptions)
                log.info("chrome browser launch successfully")
            elif browser_name=="firefox":
                firefoxoptions=FirefoxOptions()
                firefoxoptions.add_argument("start-maximize")
                driver=webdriver.Firefox(executable_path="./drivers/geckodriver.exe",options=firefoxoptions)
                log.info("firefox browser launch successfully")
            elif browser_name=="ie":
                ieoptions=IeOptions()
                ieoptions.add_argument("start-maximize")
                driver=webdriver.Ie(executable_path="./drivers/IEDriverServer.exe",options=ieoptions)
                log.info("ie browser launch successfully")
            else:
                log.error("invalid browser name")
        except WebDriverException as e:
            log.error("exception ",e)
        driver.implicitly_wait(10)
        driver.get(url)

    def identify_element(self,locater_type,locater):
        if locater_type=="id":
            return driver.find_element_by_id(locater)
        elif locater_type=="name":
            return driver.find_element_by_name(locater)
        elif locater_type=="classname":
            return driver.find_element_by_class_name(locater)
        elif locater_type=="tagname":
            return driver.find_element_by_tag_name(locater)
        elif locater_type=="linktext":
            return driver.find_element_by_link_text(locater)
        elif locater_type=="partiallinktext":
            return driver.find_element_by_partial_link_text(locater)
        elif locater_type=="css":
            return driver.find_element_by_css_selector(locater)
        elif locater_type=="xpath":
            return driver.find_element_by_xpath(locater)
        else:
            log.error("invalid locater type for identify element")


    def identify_elements(self,locater_type,locater):
        if locater_type=="id":
            return driver.find_elements_by_id(locater)
        elif locater_type=="name":
            return driver.find_elements_by_name(locater)
        elif locater_type=="classname":
            return driver.find_elements_by_class_name(locater)
        elif locater_type=="tagname":
            return driver.find_elements_by_tag_name(locater)
        elif locater_type=="linktext":
            return driver.find_elements_by_link_text(locater)
        elif locater_type=="partiallinktext":
            return driver.find_elements_by_partial_link_text(locater)
        elif locater_type=="css":
            return driver.find_elements_by_css_selector(locater)
        elif locater_type=="xpath":
            return driver.find_elements_by_xpath(locater)
        else:
            log.error("invalid locater type for identify elements")

    def perform_action_on_elements(self,element,action_type,value=None,other=None):
        return_value=None
        if action_type=="click":
            element.click()
        elif action_type=="sendkeys":
            element.clear()
            element.send_keys(value)
        elif action_type=="gettext":
            return_value=element.text
        elif action_type=="getattribute":
            element.get_attribute(value)
        elif action_type=="setattribute":
            script="document.getElementsByClassName('" + other + "')[0].value="+ value +")"
            driver.execute_script(script)
        elif action_type=="isdisplayed":
            return_value=element.is_displayed()
        elif action_type=="isselected":
            return_value=element.is_selected()
        elif action_type=="isenabled":
            return_value=element.is_enabled()
        elif action_type=="selectdropdown":
            sel=Select(element)
            if other=="index":
                sel.select_by_index(value)
            elif other=="value":
                sel.select_by_value(value)
            elif other=="visibletext":
                sel.select_by_visible_text(value)
            elif other=="options":
                return_value=sel.options
            else:
                log.error("invalid select type")
        else:
            log.error("invalid perform action type on element")
        return return_value

    def get_page_details(self,detail_type,element=None):
        return_value=None
        if detail_type=="text":
            return element.text
        elif detail_type=="title":
            return_value=driver.title
        elif detail_type=="url":
            return_value=driver.current_url
        else:
            log.error("invalid page detail type")
        return return_value

    def key_operations(self,element,key_action_type):
        if key_action_type=="down":
            element.send_keys(Keys.DOWN)
        elif key_action_type=="arrowdown":
            element.send_keys(Keys.ARROW_DOWN)
        elif key_action_type=="arrowup":
            element.send_keys(Keys.ARROW_UP)
        elif key_action_type=="arrowright":
            element.send_keys(Keys.ARROW_RIGHT)
        elif key_action_type=="arrowleft":
            element.send_keys(Keys.ARROW_LEFT)
        elif key_action_type=="space":
            element.send_keys(Keys.SPACE)
        elif key_action_type=="tab":
            element.send_keys(Keys.TAB)
        elif key_action_type=="backspace":
            element.send_keys(Keys.BACKSPACE)
        elif key_action_type=="enter":
            element.send_keys(Keys.ENTER)
        else:
            log.error("invalid key operation action type")

    def switch_to_another_object(self,object_type,value=None,other=None):
        return_value=None
        if object_type=="window":
            parent_handle=driver.current_window_handle
            all_handles=driver.window_handles
            for handle in all_handles:
                if handle!=parent_handle:
                    driver.switch_to.window(handle)
                    if driver.title==value:
                        break
                    else:
                        continue
        elif object_type=="frame":
            driver.switch_to.frame(value)
        elif object_type=="alert":
            alert=driver.switch_to.alert
            if other=="accept":
                alert.accept()
            elif other=="dismiss":
                alert.dismiss()
            elif other=="sendkeys":
                alert.send_keys(value)
            elif other=="gettext":
                return_value=alert.text
            else:
                log.error("invalid alert type")
        else:
            raise Exception
        return return_value

    def perform_mouse_keyboard_actions(self,element,action_type,source_ele=None,dest_ele=None,value=None):
        ac=ActionChains(driver)
        if action_type=="rightclick":
            ac.context_click(element)
        elif action_type=="movetoelement":
            ac.move_to_element(element)
        elif action_type=="click":
            ac.click(element)
        elif action_type=="sendkeys":
            ac.send_keys(value)
        elif action_type=="doubleclick":
            ac.double_click(element)
        elif action_type=="draganddrop":
            ac.drag_and_drop(source_ele,dest_ele)
        elif action_type=="clickandhold":
            ac.click_and_hold(element)
        elif action_type=="keyup":
            ac.key_up(value,element)
        elif action_type=="keydown":
            ac.key_down(value,element)
        else:
            log.error("invalid mause key board action type")
        ac.perform()

    def explicit_wait_method(self,condition,address,extra=None):
        wait=WebDriverWait(driver,20)
        element=None
        locater=By.XPATH,address
        if condition=="presenceofelement":
            cc=ec.presence_of_element_located(locater)
            element=wait.until(cc)
        elif condition=="elementtobeselected":
            cc=ec.element_to_be_selected(locater)
            element=wait.until(cc)
        elif condition=="elementlocatedtobeselected":
            cc=ec.element_located_to_be_selected(locater)
            element=wait.until(cc)
        elif condition=="elementtobeclickable":
            cc=ec.element_to_be_clickable(locater)
            wait.until(cc)
        elif condition=="visibilityofelementlocated":
            cc=ec.visibility_of_element_located(locater)
            wait.until(cc)
        elif condition=="titlecontains":
            cc=ec.title_contains(extra)
            element=wait.until(cc)
        elif condition=="presenceofallelementslocated":
            cc=ec.presence_of_all_elements_located(locater)
            element=wait.until(cc)
        elif condition=="visibilityof":
            cc=ec.visibility_of(element)
            element=wait.until(cc)
        else:
            log.error("invalid condition type for wait")
        return element

    def capture_screenshot(self,file_name):
        driver.save_screenshot("./screenshots/"+file_name+".png")


    def close_application(self):
        driver.quit()
        log.info("application closed")

    def nevigation_command_implementation(self,nevigation_type):
        if nevigation_type=="back":
            driver.back()
        elif nevigation_type=="forword":
            driver.forward()
        else:
            log.error("invalid nevigation type")

