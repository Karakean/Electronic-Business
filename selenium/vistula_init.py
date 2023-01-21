import json
import time 

from selenium import webdriver
from selenium.common.exceptions import TimeoutException

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

def wait_for(type, name, delay):
  try:
    WebDriverWait(driver, delay).until(EC.presence_of_element_located((type,name)))
    print ("Page is ready to use!")
  except TimeoutException:
    print("Loading is too long")
    raise

def wait_for_finish():
  WebDriverWait(driver, 20000).until(EC.element_to_be_clickable((By.ID, "import_close_button")))
  driver.find_element(By.ID, "import_close_button").click()

def login():
    email = driver.find_element(By.ID, "email")
    password = driver.find_element(By.ID, "passwd")

    email.clear()
    email.send_keys("admin@wpusc.pls")

    password.clear()
    password.send_keys("naranara")
    password.send_keys(Keys.RETURN)
    return

  

def gotoImport():
  #show menu
  wait_for(By.ID, "subtab-AdminAdvancedParameters", 20)
  subtab = driver.find_element(By.ID, "subtab-AdminAdvancedParameters")
  subtab.location_once_scrolled_into_view
  subtab.click()

  #scroll and click import
  wait_for(By.ID, "subtab-ShopParameters", 20)
  subtab = driver.find_element(By.ID, "subtab-ShopParameters")
  subtab.location_once_scrolled_into_view
  wait_for(By.LINK_TEXT, "Importuj", 20)
  driver.find_element(By.LINK_TEXT, "Importuj").click()
  return

def selectImportMode(mode):
  print("wait")
  wait_for(By.ID, "entity", 50) # Has really long wait times, often timeouts
  dropMenu = driver.find_element(By.ID, "entity")
  options = Select(dropMenu)
  options.select_by_value(mode)

  # Choose file
  wait_for(By.ID, "file",20)
  upload = driver.find_element(By.ID, "file")
  upload.location_once_scrolled_into_view
  driver.execute_script("window.scrollBy(0, -50);")
  return upload

def importCategories():
  upload = selectImportMode("5")

  upload.send_keys("/home/kulpas/Studia/Biznes/Electronic-Business/Selenium-Features/data_category.csv")
  #TUTAJ ŚCIEŻKA NA PLIK  ^^^^^^^^^^^^^^^^^^^
 
  time.sleep(5)

  # Select toggles
  btn = driver.find_element(By.ID, "truncate_1")
  btn.location_once_scrolled_into_view
  driver.execute_script("window.scrollBy(0, -150);")
  time.sleep(1)
  btn.click()

  driver.find_element(By.ID, "forceIDs_1").click()
  driver.find_element(By.ID, "sendemail_0").click()

  time.sleep(2)

  driver.find_element(By.NAME, "submitImportFile").click()
  driver.switch_to.alert.accept()

  time.sleep(2)
  # Final confirm and wait for finish
  
  final = driver.find_element(By.ID,"import")
  final.location_once_scrolled_into_view
  final.click()
  wait_for_finish()
  return

def importProducts():
  upload = selectImportMode("1")

  upload.send_keys("/home/kulpas/Studia/Biznes/Electronic-Business/Selenium-Features/data_product.csv")
  #TUTAJ ŚCIEŻKA NA PLIK  ^^^^^^^^^^^^^^^^^^^
 
  time.sleep(7)
  # Select toggles
  btn = driver.find_element(By.ID, "truncate_1")
  btn.location_once_scrolled_into_view
  driver.execute_script("window.scrollBy(0, -150);")
  time.sleep(1)
  #btn.click()

  #driver.find_element(By.ID, "forceIDs_1").click()
  #driver.find_element(By.ID, "sendemail_0").click()

  time.sleep(2)

  # Send
  driver.find_element(By.NAME, "submitImportFile").click()
  driver.switch_to.alert.accept()

  # Change one column name
  wait_for(By.ID,"import",20)
  dropdown = driver.find_element(By.NAME, "type_value[4]")
  options = Select(dropdown)
  options.select_by_value("price_tin")

  time.sleep(2)
  # Final confirm and wait for finish
  
  final = driver.find_element(By.ID,"import")
  final.location_once_scrolled_into_view
  final.click()
  wait_for_finish()
  return

def importCombinations():
  upload = selectImportMode("2")

  upload.send_keys("/home/kulpas/Studia/Biznes/Electronic-Business/Selenium-Features/data_combination.csv")
  #TUTAJ ŚCIEŻKA NA PLIK  ^^^^^^^^^^^^^^^^^^^
 
  time.sleep(7)
  # Select toggles
  btn = driver.find_element(By.ID, "truncate_1")
  btn.location_once_scrolled_into_view
  driver.execute_script("window.scrollBy(0, -150);")
  time.sleep(1)

  # Send
  driver.find_element(By.NAME, "submitImportFile").click()
  driver.switch_to.alert.accept()

  time.sleep(2)
  # Final confirm and wait for finish
  
  final = driver.find_element(By.ID,"import")
  final.location_once_scrolled_into_view
  final.click()
  wait_for_finish()
  return

driver = webdriver.Firefox()
driver.maximize_window()

driver.get("https://localhost/amdin/")

login()
# gotoImport()
# importCategories()
# importProducts()
# importCombinations()
