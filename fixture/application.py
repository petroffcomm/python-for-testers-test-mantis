# -*- coding: utf-8 -*-
from selenium import webdriver

from fixture.mantis_soap_api import MantisSoapApiHelper
from fixture.session import SessionHelper
from fixture.navigation import NavigationHelper
from fixture.mantis_project import ProjectHelper
from fixture.mantis_signup import MantisSignUpHelper
from fixture.james import JamesHelper
from fixture.mail import MailHelper


class Application:
    def __init__(self, browser, config):
        if browser == "firefox":
            self.wd = webdriver.Firefox(capabilities={"marionette": False},
                                        firefox_binary=
                                        "/media/WORK/JOB/education/software_testing/PythonForTesters/env/firefox_esr/firefox")
            #self.wd = webdriver.Firefox(capabilities={"marionette": False},
            #                            firefox_binary="/Applications/Firefox 2.app/Contents/MacOS/firefox")
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser: %s" % browser)

        self.config = config
        self.base_url = config['web']['baseUrl']

        self.session = SessionHelper(self)
        self.navigation = NavigationHelper(self)
        self.projects = ProjectHelper(self)
        self.mantis_signup = MantisSignUpHelper(self)
        self.mantis_soap_api = MantisSoapApiHelper(self)

        self.james = JamesHelper(self)
        self.mail = MailHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def destroy(self):
        self.wd.quit()
