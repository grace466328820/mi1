#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import  time
import  unittest
from  framework.browser_engine import  BrowserEngine
from  pageobjects.baidu_homepage import HomePage

class BaiduSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    '''关闭浏览器'''

    def test_baidu_search(self):
        homepage = HomePage(self.driver)
        homepage.type_search('selenium')  # 调用页面对象中的方法
        homepage.send_submit_btn()  # 调用页面对象类中的点击搜索按钮方法
        time.sleep(2)
        homepage.get_windows_img()  # 调用基类截图方法
        try:
            assert 'selenium' in homepage.get_page_title()  # 调用页面对象继承基类中的获取页面标题方法
            print('Test Pass.')
        except Exception as e:
            print('Test Fail.', format(e))

    def test_search2(self):
        homepage = HomePage(self.driver)
        homepage.type_search('python')
        homepage.send_submit_btn()
        time.sleep(2)
        homepage.get_windows_img()
if __name__ == '__main__':
    unittest.main()
