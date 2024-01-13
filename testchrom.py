from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys #нажатие кнопок
from selenium.webdriver.common.by import By #поиск элементов
url = 'https://vk.com/login?u=2&to=L2F1ZGlvczEwNjA1ODYzNw--'


service = webdriver.ChromeService(executable_path=".\\src\\drivers\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get(url)
title = driver.title


# time.sleep(2)
driver.implicitly_wait(2)
login=driver.find_element(By.CLASS_NAME,'VkIdForm__input')
login.send_keys('nikolinane@mail.ru')
button=driver.find_element(By.XPATH, '//span[@class="FlatButton__in"]').click()
passvord = driver.find_element(By.XPATH, '//input[@placeholder="Введите пароль"]')
passvord.send_keys("Anilokina1994")
driver.implicitly_wait(10)
button=driver.find_element(By.XPATH, '//span[@class="vkuiButton__in"]').click()
# time.sleep(4)
driver.implicitly_wait(10)
musik=driver.find_element(By.LINK_TEXT,"Музыка").click()
music=driver.find_element(By.)
driver.close()
driver.quit()
pass