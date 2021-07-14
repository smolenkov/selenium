from selenium.webdriver.chrome.webdriver import WebDriver

def test_yahoo_search():
    driver = WebDriver(executable_path='C://chromedriver//chromedriver.exe')
    driver.get('https://www.yahoo.com')
    print(None)
    ...