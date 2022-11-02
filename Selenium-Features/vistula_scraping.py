from selenium import webdriver
from selenium.webdriver.common.by import By


class Category:
    def __init__(self, main, category, link):
        self.main = main
        self.category = category
        self.subcategories = list()
        self.link = link

    def print(self):
        print(self.main, self.category, self.link)
        if self.subcategories:
            for subcategory in self.subcategories:
                print(subcategory.main, subcategory.category, subcategory.link)
        print()
        print()

class Product:
    def __init__(self, categories, url):
        self.code = "code"
        self.name = "name"
        self.price = "price"
        self.size = "size"
        self.discount_price = "discount_price"
        self.photos_urls = "photos_urls"
        self.description = "description"
        self.categories = categories
        self.details = "details"
        self.material = "material"
        self.url = url


PATH = "C:\\Drive\\chromeDriver\\chromedriver.exe"
driver = webdriver.Chrome(PATH)

SHOP_PATH = "https://vistula.pl/"
SUBPAGES = ['mezczyzna', 'kobieta']
#NUM_OF_PAGES = [18, 3]
NUM_OF_PAGES = [1, 1]
PRODUCT_LINKS = list()
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
            CATEGORIES.append(Category(SUBPAGES[i], certain_category.text, certain_category.get_attribute("href")))
        except:
            pass

for category in CATEGORIES:
    driver.get(category.link)
    subcategories = driver.find_elements(by=By.CLASS_NAME, value="sidebarChildrenCategory")
    if subcategories:
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
                    PRODUCT_LINKS.append(Product(subcategory, product.get_attribute("href")))
                except:
                    pass
    else:
        driver.get(category.link)
        page = driver.find_element(by=By.CLASS_NAME, value="product-page-items")
        products = page.find_elements(by=By.CSS_SELECTOR, value="a")
        for product in products:
            try:
                PRODUCT_LINKS.append(Product(category, product.get_attribute("href")))
            except:
                pass


# for i in range(len(SUBPAGES)):
#     for j in range(NUM_OF_PAGES[i]):
#         driver.get(SHOP_PATH + SUBPAGES[i] + '?page=' + str(j + 1))
#         page = driver.find_element(by=By.CLASS_NAME, value="product-page-items")
#         products = page.find_elements(by=By.CSS_SELECTOR, value="a")
#         for product in products:
#             try:
#                 PRODUCT_LINKS.append(product.get_attribute("href"))
#             except:
#                 pass


PRODUCTS = list()
for product in PRODUCT_LINKS:
    driver.get(product)

    try:
        product_code_div = driver.find_element(by=By.CLASS_NAME, value="product-code")
        product_code = product_code_div.find_element(by=By.CSS_SELECTOR, value="h2").text.replace('KOD PRODUKTU: ', '')
        print(product_code)
    except:
        pass

    try:
        title_div = driver.find_element(by=By.CLASS_NAME, value="product-title")
        title = title_div.find_element(by=By.CSS_SELECTOR, value="h1").text
        print(title)
    except:
        pass

    try:
        price_div = driver.find_element(by=By.CLASS_NAME, value="product-price")
        price = price_div.find_element(by=By.CSS_SELECTOR, value="span").text.replace(' ZŁ', '')
        print(price)
    except:
        pass

    # try:
    #     #size placeholder
    # except:
    #     pass
    #
    # try:
    #     #discount price placeholder
    # except:
    #     pass
    #
    # try:
    #     #photos placeholder
    # except:
    #     pass
