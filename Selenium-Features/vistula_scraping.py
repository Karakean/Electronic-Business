import json

from selenium import webdriver
from selenium.webdriver.common.by import By


class Category:
    def __init__(self, main, category, link):
        self.main = main
        self.category = category
        self.subcategories = list()
        self.link = link

class Product:
    def __init__(self, categories, url):
        self.categories = categories
        self.url = url
        self.code = None
        self.name = None
        self.price = None
        self.without_discount_price = None
        self.details = list()
        self.photos_urls = list()
        self.size = list()


PATH = "C:\\Drive\\chromeDriver\\chromedriver.exe"
driver = webdriver.Chrome(PATH)

SHOP_PATH = "https://vistula.pl/"
SUBPAGES = ['mezczyzna', 'kobieta']
PRODUCTS = list()
CATEGORIES = list()

driver.get(SHOP_PATH + SUBPAGES[0])
try:
    cookie = driver.find_element(by=By.ID, value="acceptAllCookiesBottom")
    cookie.click()
except:
    pass

for i in range(len(SUBPAGES)):
    driver.get(SHOP_PATH + SUBPAGES[i])
    categories = driver.find_elements(by=By.CLASS_NAME, value="sidebarChildrenCategory ")
    for category in categories:
        try:
            certain_category = category.find_element(by=By.CSS_SELECTOR, value="a")
            CATEGORIES.append(Category(SUBPAGES[i].upper(), certain_category.text, certain_category.get_attribute("href")))
        except:
            pass

for category in CATEGORIES:
    driver.get(category.link)
    subcategories = driver.find_elements(by=By.CLASS_NAME, value="sidebarChildrenCategory")
    if subcategories and category.category != "JEANSY": #sidecase wrong website implementation
        for subcategory in subcategories:
            try:
                certain_subcategory = subcategory.find_element(by=By.CSS_SELECTOR, value="a")
                category.subcategories.append(Category(category.main+"/"+category.category, certain_subcategory.text, certain_subcategory.get_attribute("href")))
            except:
                pass

for category in CATEGORIES:
    if category.subcategories:
        for subcategory in category.subcategories:
            driver.get(subcategory.link)
            page = driver.find_element(by=By.CLASS_NAME, value="product-page-items")
            products = page.find_elements(by=By.CSS_SELECTOR, value="a")
            for product in products:
                try:
                    PRODUCTS.append(Product(subcategory, product.get_attribute("href")))
                except:
                    pass
    else:
        driver.get(category.link)
        page = driver.find_element(by=By.CLASS_NAME, value="product-page-items")
        products = page.find_elements(by=By.CSS_SELECTOR, value="a")
        for product in products:
            try:
                PRODUCTS.append(Product(category, product.get_attribute("href")))
            except:
                pass

print(len(PRODUCTS))
for product in PRODUCTS:
    driver.get(product.url)

    try:
        product_code_div = driver.find_element(by=By.CLASS_NAME, value="product-code")
        product_code = product_code_div.find_element(by=By.CSS_SELECTOR, value="h2").text.replace('KOD PRODUKTU: ', '')
        product.code = product_code
    except:
        pass

    try:
        title_div = driver.find_element(by=By.CLASS_NAME, value="product-title")
        title = title_div.find_element(by=By.CSS_SELECTOR, value="h1").text
        product.name = title
    except:
        pass

    try:
        price_div = driver.find_element(by=By.CLASS_NAME, value="product-price")
        price = price_div.find_element(by=By.CSS_SELECTOR, value="span").text.replace(' ZŁ', '')
        product.price = price
    except:
        pass

    try:
        price_div = driver.find_element(by=By.CLASS_NAME, value="product-price")
        price = price_div.find_element(by=By.CSS_SELECTOR, value="del").text.replace(' ZŁ', '')
        if price:
            product.without_discount_price = price
    except:
        pass

    try:
        details = driver.find_elements(by=By.CLASS_NAME, value="product-description-text")
        for detail in details:
            product.details.append(detail.text)
    except:
        pass

    try:
        photos_div = driver.find_elements(by=By.CLASS_NAME, value="open-gallery")
        for photo_div in photos_div:
            photo = photo_div.find_element(by=By.CSS_SELECTOR, value="img")
            product.photos_urls.append(photo.get_attribute("src"))
    except:
        pass

    try:
        size_div = driver.find_element(by=By.CLASS_NAME, value="select-items")
        sizes = size_div.find_elements(by=By.CLASS_NAME, value="noselect")
        for size in sizes:
            product.size.append(size.get_attribute('innerHTML').replace(' <i class="fas fa-sm fa-info-circle"></i>', ''))
    except:
        pass

PRODUCTS_DICTIONARY = {f"product{i}": {
                            "category": f"{PRODUCTS[i].categories.main}/{PRODUCTS[i].categories.category}",
                            "url": PRODUCTS[i].url,
                            "code": PRODUCTS[i].code,
                            "name": PRODUCTS[i].name,
                            "price": PRODUCTS[i].price,
                            "without_discount_price": PRODUCTS[i].without_discount_price,
                            "details": PRODUCTS[i].details,
                            "photos_urls": PRODUCTS[i].photos_urls,
                            "size": PRODUCTS[i].size} for i in range(len(PRODUCTS))}

with open("data.json", "w", encoding="utf-8") as outfile:
    json.dump(PRODUCTS_DICTIONARY, outfile, ensure_ascii=False, indent=2)
