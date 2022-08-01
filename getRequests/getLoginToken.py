#Code that generates Login Token Needed to make HTTP requests  
from seleniumwire import webdriver as ww  
from selenium import webdriver  
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time 
from wsproto import Headers

class getToken:

    def seleniumLogin(self):    
        self.a = ""
        loginUrl = 'https://justinbauerfitness.trainerize.com/app/logon.aspx'
        username = 'jesse@justinbauerfitness.com'
        password = 'JesseJesse45' 
        wait_time_out = 7
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging']) 
        driver = ww.Chrome(options=options)  
        wait_variable = WebDriverWait(driver, wait_time_out)
        
        #Log into my account 

        driver.get(loginUrl)
        
        wait_variable.until(EC.element_to_be_clickable((By.ID, "t_user"))) 
        elem = driver.find_element(By.ID, "t_user")  
        elem.send_keys(username)

        elem = driver.find_element(By.ID, "t_pwd")  
                
        elem.send_keys(password)
        elem.send_keys(Keys.RETURN) 

        # Navigate to Client Folder
        
        wait_variable.until(EC.element_to_be_clickable((By.ID, "nav_clients")))
    

        for request in driver.requests:
            if request.response:
                if "getClientList" in request.url:
            
                    # print(
                    #     # "URL: ", request.url, 
                    #      request.headers['Authorization']
                    #  )
                    return request.headers['Authorization']
                    break
  