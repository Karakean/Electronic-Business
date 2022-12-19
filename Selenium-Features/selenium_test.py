from faker import Faker
from random import randint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from time import sleep

def wait_for(type, name, delay):
  try:
    WebDriverWait(driver, delay).until(EC.presence_of_element_located((type,name)))
    #print ("Page is ready to use!")
  except TimeoutException:
    print("Loading is too long")
    raise

faker = Faker('PL')

PATH = "C:\Drive\chromeDriver\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("http://localhost:8080")
driver.find_element(By.CLASS_NAME, "user-info").click()
driver.find_element(By.CLASS_NAME, "no-account").click()

#register

driver.find_element(By.ID, "field-id_gender-1").click()
driver.find_element(By.ID, "field-firstname").send_keys(faker.first_name())
driver.find_element(By.ID, "field-lastname").send_keys(faker.last_name())
driver.find_element(By.ID, "field-email").send_keys(faker.email())
driver.find_element(By.ID, "field-password").send_keys(faker.password())
driver.find_element(By.ID, "field-birthday").send_keys(faker.date())

elements = driver.find_elements(By.CLASS_NAME, "custom-checkbox")
for elem in elements:
    elem.click()

driver.find_element(By.CLASS_NAME, "form-control-submit").click()

#add products


driver.find_element(By.CLASS_NAME, "thumbnail-top").click()

wait_for(By.CLASS_NAME, "add-to-cart, btn, btn-primary", 10)
element = driver.find_element(By.CLASS_NAME, "add-to-cart, btn, btn-primary")
element.location_once_scrolled_into_view
element.click()

sleep(1)

driver.refresh()


wait_for(By.CLASS_NAME, "product", 10)
products = driver.find_elements(By.CLASS_NAME, "product")


products_list = list()
for product in products:
    certain_product = product.find_element(By.CSS_SELECTOR, value="a")
    products_list.append(certain_product)

for product in products_list[:4]:
    product.click()
    wait_for(By.CLASS_NAME, "add-to-cart, btn, btn-primary", 10)
    element = driver.find_element(By.CLASS_NAME, "add-to-cart, btn, btn-primary")
    element.location_once_scrolled_into_view
    element.click()
    sleep(1)
    driver.back()
    sleep(1)
    driver.back()
    sleep(10)

#other category

driver.find_element(By.ID, "category-147").click()
driver.find_element(By.CLASS_NAME, "subcategory-image").click()
products = driver.find_elements(By.CLASS_NAME, "thumbnail-top")

products_list = list()
for product in products:
    products_list.append(product)

for product in products_list[:5]:
    product.click()
    wait_for(By.CLASS_NAME, "add-to-cart, btn, btn-primary", 10)
    element = driver.find_element(By.CLASS_NAME, "add-to-cart, btn, btn-primary")
    element.location_once_scrolled_into_view
    element.click()
    sleep(1)
    driver.back()
    sleep(1)
    driver.back()
    sleep(10)

#shopping cart
driver.find_element(By.CLASS_NAME, "shopping-cart").click()

#remove 1 item
driver.find_element(By.CLASS_NAME, "remove-from-cart").click()

#proceed
driver.find_element(By.CLASS_NAME, "cart-detailed-actions").click()

driver.find_element(By.ID, "field-address1").send_keys(faker.addres())
driver.find_element(By.ID, "field-postcode").send_keys(str(randint(10, 99))+'-'+str(randint(100,999)))
driver.find_element(By.ID, "field-city").send_keys(faker.city())

driver.find_element(By.NAME, "confirm-addresses").click()
driver.find_element(By.NAME, "confirmDeliveryOption").click()

driver.find_element(By.ID, "payment-option-1-container").click()
driver.find_element(By.ID, "conditions_to_approve[terms-and-conditions]").click()
driver.find_element(By.CLASS_NAME, "btn.btn-primary.center-block").click()

#check status
driver.find_element(By.CLASS_NAME, "account").click()
driver.find_element(By.ID, "history-link").click()






