from selenium import webdriver
from selenium.webdriver.common.by import By


PATH = "C:\\Drive\\chromeDriver\\chromedriver.exe"
driver = webdriver.Chrome(PATH)

SHOP_PATH = "https://vistula.pl/"
SUBPAGES = ['mezczyzna', 'kobieta']
NUM_OF_PAGES = [18, 3]
SUBPAGE = 1
PRODUCT_LINKS = list()

for i in range(len(SUBPAGES)):
    for j in range(NUM_OF_PAGES[i]):
        driver.get(SHOP_PATH + SUBPAGES[i] + '?page=' + str(j+1))
        try:
            cookie = driver.find_element(by=By.ID, value="acceptAllCookiesBottom")
            cookie.click()
        except:
            pass
        page = driver.find_element(by=By.CLASS_NAME, value="product-page-items")
        products = page.find_elements(by=By.CSS_SELECTOR, value="a")
        for product in products:
            try:
                PRODUCT_LINKS.append(product.get_attribute("href"))
            except:
                pass

for product in PRODUCT_LINKS:
    print(product)

print(len(PRODUCT_LINKS))
