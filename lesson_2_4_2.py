import math
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))
try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    button = browser.find_element(By.ID,"book")
    WebDriverWait(browser,15).until(
    	EC.text_to_be_present_in_element((By.ID,"price"), "100")
    	)
    button.click()
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    x_el=browser.find_element_by_id('input_value')
    x=x_el.text    	
    y=calc(x)
    browser.find_element_by_id('answer').send_keys(y)
    #button = browser.find_element_by_css_selector("button.btn")
    button = browser.find_element(By.ID,"solve")
    button.click()
    time.sleep(2)
    alert = browser.switch_to.alert
    alert_text = alert.text
    print(alert_text)
    alert.accept()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
