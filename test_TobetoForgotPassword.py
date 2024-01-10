from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait #ilgili driverı bekleten yapı
from selenium.webdriver.support import expected_conditions as ec #beklenen koşullar
import pytest
import openpyxl
from constants import globalConstants as c


class Test_TobetoForgotPassword:
    def setup_method(self): #her test başlangıcında çalışacak fonk
       self.driver = webdriver.Chrome()
       self.driver.get(c.FORGOT_PASSWORD_URL)
       self.driver.maximize_window()
       sleep(3)  # import time

    def teardown_method(self): # her testinin bitiminde çalışacak fonk
       self.driver.quit()    

    def getData():
       excel = openpyxl.load_workbook(c.LOGIN_TOBETO_XLSX)
       sheet = excel["Sheet4"] #hangi sayfada çalışacağımı gösteriyorum
       data = []
       email = sheet.cell(row=2, column=1).value
       data.append((email))

       return data
      
    @pytest.mark.parametrize("email",getData())
    def test_forgot_password(self,email):
        forgotPasswordInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,c.FORGOT_PASSWORD)))
        forgotPasswordInput.send_keys(email)
        sleep(3)
        gonder = self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/section/div/div/div/button")
        gonder.click()
        sleep(3)
        toast_message = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.XPATH, "//div[@class='toast-body']")))
        assert toast_message.text == "• Girdiğiniz e-posta geçersizdir." 
        sleep(3)
       

