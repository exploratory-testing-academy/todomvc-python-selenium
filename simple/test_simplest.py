from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def test_simplest():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://todomvc.com/examples/vanillajs/")
    input_field = driver.find_element(By.CLASS_NAME, "new-todo")
    input_field.send_keys("Learning Selenium")
    input_field.send_keys(Keys.ENTER)
    assert driver.find_element(By.CSS_SELECTOR, ".todo-list li label").text == "Learning Selenium"