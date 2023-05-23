import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_Options = webdriver.ChromeOptions()
chrome_Options.add_argument("headless")


class Test_Py:

    @pytest.mark.xfail
    def test_sum_001(self):
        a = 3
        b = 5
        sum = a + b
        print(sum)
        if sum == 8:
            print("test_sum_001 is passed")
        else:
            print("test_sum_001 is failed")


    def test_mul_002(self):
        a = 3
        b = 5
        mul = a * b
        print(mul)
        if mul == 16:
            print("test_mul_002 is passed")
            assert True
        else:
            print("test_mul_002 is failed")
            assert False

    def _sum_003(self):
        a = 3
        b = 5
        sum = a + b
        print(sum)
        if sum == 16:
            print("test_sum_003 is passed")
            assert True
        else:
            print("test_sum_003 is failed")
            assert False

    @pytest.mark.group1
    def test_Google(self):

        #driver = webdriver.Chrome()
        driver = webdriver.Chrome(options=chrome_Options)
        driver.get("https://www.google.com/")
        # time.sleep(2)
        logo = driver.find_element(By.XPATH, "//img[@class='lnXdpd']").is_displayed()
        print(logo)
        if logo == True:
            driver.close()
            assert True
        else:
            driver.close()
            assert False







