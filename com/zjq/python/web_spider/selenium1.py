# Selenium 是web自动化测试工具集，爬虫可以利用其实现对页面动态资源的采集。请按顺序操作
#
# 安装 Python Selenium 包：pip install selenium
# 安装 Chrome 驱动：https://npm.taobao.org/mirrors/chromedriver/，如果使用别的浏览器需要下载对应浏览器的驱动
# 编写使用 python unittest 测试使用 selenium 完成自动化
# selenium 自动化网页测试的操作：
#
# 使用 selenium 的Chrome 驱动，打开 CSDN 首页，此时会打开 Chrome 浏览器测试页面
# 验证字符串 "CSDN" 在页面标题
# 找到网页里的搜索框
# 输入"OpenCV技能树"
# 输入回车，搜索结果
# 等待10秒退出
# 代码框架如下：

# -*- coding: UTF-8 -*-
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    # 实现浏览器自动化测试需求
    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://www.csdn.net/")
        self.assertIn("CSDN", driver.title)

        elem = driver.find_element(By.ID,"toolbar-search-input")
        elem.send_keys("OpenCV 技能树")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source
        time.sleep(10)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()