from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://portal.spacebasic.com/login")

time.sleep(2)

email_field = driver.find_element(By.NAME, "email")
email_field.send_keys("YOUR_EMAIL")

password_field = driver.find_element(By.NAME, "password")
password_field.send_keys("YOUR_PASSWORD")


login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()


time.sleep(8)
driver.get("https://portal.spacebasic.com/module/complaints")
time.sleep(8)

addComplaint = driver.find_element(By.ID, "addComplaintbtn")
addComplaint.click()
time.sleep(8)

wait = WebDriverWait(driver, 10)

dropdown = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//ng-select[@placeholder='Please select a category']//div[contains(@class, 'ng-select-container')]"))
)
dropdown.click()

option = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "(//span[contains(text(),'Housekeeping')])[1]"))
)
option.click()

dropdown = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//ng-select[@name='subCategory']//div[contains(@class, 'ng-select-container')]"))
)
dropdown.click()

option = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "(//span[contains(text(),'Room and Bathroom Cleaning')])[1]"))
)
option.click()

dropdown = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//ng-select[@name='assign']//div[contains(@class, 'ng-select-container')]"))
)
dropdown.click()

option = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "(//span[contains(text(),'Critical')])[1]"))
)
option.click()



time.sleep(8)




print("Page title:", driver.title)

driver.quit()
