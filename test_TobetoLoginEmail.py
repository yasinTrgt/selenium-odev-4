from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait #ilgili driverı bekleten yapı
from selenium.webdriver.support import expected_conditions as ec #beklenen koşullar
import pytest
import openpyxl
from constants import globalConstants as c


class Test_tobetoLoginEmail:
    def setup_method(self): #her test başlangıcında çalışacak fonk
        self.driver = webdriver.Chrome()
        self.driver.get(c.BASE_URL)
        self.driver.maximize_window()
        sleep(3)  # import time
    
    def teardown_method(self): # her testinin bitiminde çalışacak fonk
           self.driver.quit()  


    def getData():
        excel = openpyxl.load_workbook(c.LOGIN_TOBETO_XLSX)
        sheet = excel["Sheet2"] #hangi sayfada çalışacağımı gösteriyorum
        rows = sheet.max_row #kaçıncı satıra kadar veri var?
        data = []
        for i in range(2,rows+1):
            email = sheet.cell(i,1).value
            password = sheet.cell(i,2).value
            data.append((email,password))

        return data

    @pytest.mark.parametrize("email,password",getData())
    def test_login(self,email,password):
        loginButton = self.driver.find_element(By.LINK_TEXT, "Giriş Yap")
        loginButton.click()
        sleep(3) 
        usernameInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.NAME,c.E_MAIL)))
        usernameInput.send_keys(email)
        passwordInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.NAME,c.PASSWORD_NAME)))
        passwordInput.send_keys(password)
        loginButtonClick= self.driver.find_element(By.XPATH,c.LOGIN_BUTTON_CLICK_XPATH)
        loginButtonClick.click()
        errorMessage = self.driver.find_element(By.LINK_TEXT,c.DOLDURULMASI_ZORUNLU_ALAN)
        assert errorMessage.text == c.DOLDURULMASI_ZORUNLU_ALAN_KONTROL      
        sleep(3)      
        
         