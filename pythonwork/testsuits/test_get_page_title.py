#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest
from  framework.browser_engine import  BrowserEngine
from  pageobjects.baidu_homepage import HomePage


class GetPageTitle(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_get_title(self):

        homapage = HomePage(self.driver)
        print(homapage.get_page_title())