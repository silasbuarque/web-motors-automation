import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get('https://www.cockpit.com.br/')

campo_email = driver.find_element(By.XPATH, "//input[@id='Email']")
campo_email.send_keys('email@email')

campo_password = driver.find_element(By.XPATH, "//input[@id='Senha']")
campo_password.send_keys('senha123')

campo_enter = driver.find_element(By.XPATH, "//button[@id='submitLoginButton']")
campo_enter.click()

sleep(10)
driver.close()