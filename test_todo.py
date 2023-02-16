from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions
from time import sleep

def test_add_basic_todo(driver):
    #basic instructions outdated
    driver.find_element(by=By.CLASS_NAME, value="new-todo").send_keys("Very Important\n")
    assert driver.find_element(By.CSS_SELECTOR, ".todo-list li label").text == "Very Important"
    #assert driver.find_elements(By.TAG_NAME, "label")[1].text == "Very Important"


def test_add_todo(driver):
    #repeat 5 times
    for i in range(5):
        driver.find_element(By.CLASS_NAME, "new-todo").send_keys(f"Test todo {i}\n")
    assert len(driver.find_elements(By.CSS_SELECTOR, ".toggle")) == 5
    driver.find_elements(By.CSS_SELECTOR, ".toggle")[3].click()
    sleep(2)
    driver.get_screenshot_as_file('sample_screenshot.png')
    assert len(driver.find_elements(By.CSS_SELECTOR, ".toggle")) == 5
    driver.find_element(By.CSS_SELECTOR, "[href='#/active']").click()
    assert len(driver.find_elements(By.CSS_SELECTOR, ".toggle")) == 4