from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.get('https://rozetka.com.ua')

def func(search_string, threshold = 5):
    search_fields = driver.find_elements(By.XPATH, "//input[@type='text'][@name='search']")
    assert len(search_fields) == 1
    if search_fields[0].text != "":
        search_fields[0].clear()
    search_fields[0].send_keys(search_string)
    buttons = driver.find_elements(By.XPATH, "//form/button")
    assert len(buttons) == 1
    buttons[0].click()
    time.sleep(15)
    items = driver.find_elements(By.XPATH, "//rz-grid/ul/li")
    filtered_items = []
    for item in items:
        comment_amount_spans = item.find_elements(By.XPATH, ".//rz-rating-review-block/a/span")
        assert len(comment_amount_spans) == 1
        try:
            n_comments = int(comment_amount_spans[0].text)
        except:
            n_comments = 0
        if n_comments >= threshold:
            filtered_items.append(item)
    return filtered_items