from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Define driver, option, and services
chrome_options = Options()
chrome_options.add_argument("--disable-search-engine-choice-screen")
service = Service('chromedriver-linux64/chromedriver')
driver = webdriver.Chrome(options=chrome_options, service=service)

# Load the webpage
driver.get("https://demoqa.com/login")

# Locate username, password and login button
username_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))
password_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'password')))
login_button = driver.find_element(By.ID, "login")
# login_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'login')))

# Fill in username and password, and click the button
username_field.send_keys("perzak102")
password_field.send_keys("PythonStudent123$")
driver.execute_script("arguments[0].click();", login_button)
# login_button.click()


input("Please Enter to close he browser")
driver.quit()