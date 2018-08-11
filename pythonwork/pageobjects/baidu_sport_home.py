#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from  framework.base_page import BasePage

class SportNewHomepage(BasePage):
    nba_link = "xpath=>//*[@id='col_focus']/div[1]/div[2]/div/div[2]/div/ul/li[1]/a"

    def click_nba_lick(self):
        self.click(self.nba_lick())
        self.sleep(2)