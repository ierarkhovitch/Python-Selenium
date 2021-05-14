#!/usr/bin/env python

from .base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.fidn_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()
