from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions
from time import sleep

def test_add_todo(driver):
    #repeat 5 times
    for i in range(5):
        driver.find_element(By.CLASS_NAME, "new-todo").send_keys("Test todo" + str(i) + "\n")
    assert len(driver.find_elements(By.CSS_SELECTOR, ".toggle")) == 5
    driver.find_element(By.CSS_SELECTOR, ".toggle").click()
    driver.get_screenshot_as_file('sample_screenshot.png')
    assert len(driver.find_elements(By.CSS_SELECTOR, ".toggle")) == 5
    driver.find_element(By.CSS_SELECTOR, "[href='#/active']").click()
    assert len(driver.find_elements(By.CSS_SELECTOR, ".toggle")) == 4