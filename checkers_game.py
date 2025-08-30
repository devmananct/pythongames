import time

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://www.gamesforthebrain.com/game/checkers/"

driver = webdriver.Chrome()
driver.get(URL)

try:
    # Wait up to 15s until the text "Select an orange piece to move." appears
    WebDriverWait(driver, 15).until(
        EC.text_to_be_present_in_element(
            (By.TAG_NAME, "body"),
            "Select an orange piece to move."
        )
    )
    print("Text found: 'Select an orange piece to move --Game loaded correctly'.'")
except:
    raise AssertionError(" Game is not loaded")

# Wait for the element and click it
#select first move
element = WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable((By.NAME, 'space62'))
)
element.click()

time.sleep(5)
#move first move
element = WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable((By.NAME, 'space73'))
)
element.click()
time.sleep(5)
#select second move
# Wait for the element and click it
element = WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable((By.NAME, 'space71'))
)
element.click()
time.sleep(5)
#make second move
element = WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable((By.NAME, 'space62'))

)
element.click()

time.sleep(5)
#select third move
element = WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable((By.NAME, 'space60'))

)
element.click()
time.sleep(5)
#make third move

element = WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable((By.NAME, 'space71'))

)
element.click()
time.sleep(5)

#select forth move
element = WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable((By.NAME, 'space22'))

)
element.click()
time.sleep(5)

#make forth move
element = WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable((By.NAME, 'space33'))

)
element.click()
time.sleep(5)

#select fifth move
element = WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable((By.NAME, 'space02'))

)
element.click()
time.sleep(5)

#make fifth move
element = WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable((By.NAME, 'space24'))

)
element.click()
time.sleep(15)
try:
    driver.find_element(By.LINK_TEXT, "Restart...").click()
except Exception:
    driver.find_element(By.PARTIAL_LINK_TEXT, "Restart").click()

try:
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.ID, "message"), "Select an orange piece to move.")
    )
    print("Game Restarted Successfully")
except TimeoutException:
    raise AssertionError(" Game Restarted Failed")
time.sleep(20)
driver.quit()
