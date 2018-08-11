#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import  time
import  unittest
from  framework.browser_engine import BrowserEngine
from  pageobjects.baidu_homepage import HomePage
from  pageobjects.baidu_news_home import NewsHomePage
from  pageobjects.baidu_sport_home import SportNewHomepage

class ViewNBANews(unittest.TestCase):
    def setUp(self):
        browse =BrowserEngine(self)
        self.driver = browse.open_browser(self)

    def tearDown(self):
        self.driver.quit()

    def test_view_nab_views(self):
        baiduhome = HomePage(self.driver)
        #baiduhome.click_news()
        #初始化百度新闻对象，点击体育
        self.driver.find_element_by_xpath("//*[@id='u1']/a[1]").click()
        newshome = NewsHomePage(self.driver)
        #newshome.click_sports()
        self.driver.find_element_by_xpath("//*[@id='channel-all']/div/ul/li[7]/a").click()
        time.sleep(2)
        #初始化一个体育新闻主页，点击NBA
        sportnewhome = SportNewHomepage(self.driver)
        #sportnewhome.click_nba_lick()
        self.driver.find_element_by_xpath("//*[@id='col_focus']/div[1]/div[2]/div/div[2]/div/ul/li[1]/a").click()
        time.sleep(2)
        sportnewhome.get_windows_img()

if __name__ == '__main__':
    unittest.main()