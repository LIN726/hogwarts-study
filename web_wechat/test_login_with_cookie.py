import shelve
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestCookies():
    def setup(self):
        options = Options()
        options.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome()

    def teardown(self):
        self.driver.quit()

    def test_cookie(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        # sleep(10)
        db = shelve.open('cookies')
        # db['cookie'] = self.driver.get_cookies()
        cookies = db.get('cookie')

        db.close()
        for cookie in cookies:
            if 'expiry' in cookie:
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        expected_conditions.invisibility_of_element_located((By.CSS_SELECTOR, "#menu_contacts > span"))
        self.driver.find_element(By.CSS_SELECTOR, "#menu_contacts > span").click()

        sleep(5)
