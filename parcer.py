from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.edge.service import service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# запуск браузера
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://quotes.toscrape.com/")


WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "quote"))
)

quotes = driver.find_elements(By.CLASS_NAME, "quote")

for box in quotes:
    text = box.find_element(By.CLASS_NAME, "text").text
    print("Цитата:", text)