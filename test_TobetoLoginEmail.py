from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait #ilgili driverı bekleten yapı
from selenium.webdriver.support import expected_conditions as ec #beklenen koşullar
import pytest
import openpyxl
from constants import globalConstants as c


class Test_TobetoLoginEmail:
   def setup_method(self): #her test başlangıcında çalışacak fonk
        self.driver = webdriver.Chrome()
        self.driver.get(c.BASE_URL)
        self.driver.maximize_window()
        sleep(3)  # import time
    
   def teardown_method(self): # her testinin bitiminde çalışacak fonk
        self.driver.quit()  

  
   def test_invalid_login(self):
       loginButton = self.driver.find_element(By.LINK_TEXT, "Giriş Yap")
       loginButton.click()
       sleep(3) 
       loginButtonClick= self.driver.find_element(By.XPATH,c.LOGIN_BUTTON_CLICK_XPATH)
       loginButtonClick.click()
       errorMessage = self.driver.find_element(By.XPATH,c.DOLDURULMASI_ZORUNLU_ALAN)
       assert errorMessage.text == c.DOLDURULMASI_ZORUNLU_ALAN_KONTROL
       sleep(3)