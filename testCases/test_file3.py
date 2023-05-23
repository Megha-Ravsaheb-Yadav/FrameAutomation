import time

from selenium import webdriver
from selenium.webdriver.common.by import By
chrome_Options = webdriver.ChromeOptions()
chrome_Options.add_argument("headless")


class Test_002:

    def test_sum_005(self):
        a = 3
        b = 4
        sum = a + b
        if sum == 7:
            assert True
        else:
            assert False

    def test_credence1(self):

        # driver = webdriver.Chrome()
        driver = webdriver.Chrome(options=chrome_Options)
        driver.get("https://credence.in/")
        offers = driver.find_element(By.XPATH, "//span[@class='text-white b label']").text
        print(offers)
        print(driver.title)
        if driver.title == "Credence":
            assert True
        else:
            assert False

    def test_credence(self):

        # driver = webdriver.Chrome()
        driver = webdriver.Chrome(options=chrome_Options)
        driver.get("https://credence.in/")
        time.sleep(2)
        driver.find_element(By.XPATH, "//img[@src='/website/images/enquiry.png']").click()
        time.sleep(2)
        l = len(driver.find_elements(By.XPATH, "//div[@class='quickfinder-description gem-text-output']//p//a"))
        print(l)
        list = []
        for r in range(1,l+1):
            contact = driver.find_element(By.XPATH, "//div[@class='quickfinder-description gem-text-output']//p//a["+str(r)+"]").text
            #print(contact)
            list.append(contact)
        if "+91 9091929355" in list:
            assert True
        else:
            assert False











