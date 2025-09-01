from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

url = "https://ozh.github.io/cookieclicker/"
driver.get(url)

try:
    consent = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "fc-primary-button"))
    )
    consent.click()
except:
    print("No consent popup found.")

cookie = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.ID, "bigCookie"))
)

def update():
    products = driver.find_elements(By.CSS_SELECTOR, "#products .enabled")
    for product in products[::-1]:
        try:
            product.click()
        except:
            pass


time_last = time.time()
while True:
    cookie.click()
    if time.time() - time_last > 5:
        update()
        time_last = time.time()
    
    time.sleep(0.001)