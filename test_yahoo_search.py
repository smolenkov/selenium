from selenium import webdriver
import time



try:
    link = "https://www.yahoo.com"
    browser = webdriver.Chrome()
    browser.get(link)

    input_field = browser.find_element_by_css_selector('#ybar-search-box-container input[type="text"]')
    query = "New York"
    input_field.send_keys(query)
    send_button = browser.find_element_by_css_selector('#ybar-search')
    send_button.click()

finally:
    time.sleep(10)
    browser.quit()