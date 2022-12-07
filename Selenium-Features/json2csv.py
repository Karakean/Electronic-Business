# ODPALAJ ZE ŚRODKA FOLDERU ./Selenium-Features

import json
import csv
import random

def clean_name(s):
    def clean_word(s):
        return s.replace(',',' &').capitalize() if len(s) > 1 else s.lower()
    
    return ' '.join([clean_word(y) for y in s.split(' ')])

def clean_catpath(cats):
    cats = cats.split("/")
    if cats[0] == "MEZCZYZNA":
        for i in range(1, len(cats)):
            cats[i] += " (MESKIE)"

    if cats[0] == "KOBIETA":
        for i in range(1, len(cats)):
            cats[i] += " (DAMSKIE)"

    return "/".join(cats)
    

jf = open('data.json')
data = json.load(jf)
jf.close()

with open('data_product.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=';',quoting=csv.QUOTE_NONNUMERIC,escapechar='$')

    writer.writerow([
        "ID",
        "Aktywny (0 lub 1)",
        "Nazwa",
        "Kategorie (x,y,z...)",
        "Cena bez podatku. (netto)",
        "ID reguły podatku",
        "Koszt własny", #filler
        "W sprzedaży (0 lub 1)",
        "Wartość rabatu",
        "Procent rabatu", #filler
        "Rabat od dnia (rrrr-mm-dd)", #filler
        "Rabat do dnia (rrrr-mm-dd)", #filler
        "Indeks #",
        "Kod dostawcy", #filler
        "Dostawca", #filler
        "Marka", #filler
        "kod EAN13", #filler
        "Kod kreskowy UPC", #filler
        "MPN", #filler
        "Podatek ekologiczny", #filler
        "Szerokość", #filler
        "Wysokość", #filler
        "Głębokość", #filler
        "Waga", #filler
        "Czas dostawy produktów dostępnych w magazynie:", #filler
        "Czas dostawy wyprzedanych produktów z możliwością rezerwacji:", #filler
        "Ilość",
        "Minimalna ilość",
        "Niski poziom produktów w magazynie",
        "Wyślij do mnie e-mail, gdy ilość jest poniżej tego poziomu", #filler
        "Widoczność",
        "Dodatkowe koszty przesyłki", #filler
        "Jednostka dla ceny za jednostkę", #filler
        "Cena za jednostkę", #filler
        "Podsumowanie",
        "Opis",
        "Tagi (x,y,z...)", #filler
        "Meta-tytuł", #filler
        "Słowa kluczowe meta", #filler
        "Opis meta", #filler
        "Przepisany URL", #filler
        "Etykieta, gdy w magazynie",
        "Etykieta kiedy dozwolone ponowne zamówienie",
        "Dostępne do zamówienia (0 = Nie, 1 = Tak)",
        "Data dostępności produktu", #filler
        "Data wytworzenia produktu", #filler
        "Pokaż cenę (0 = Nie, 1 = Tak)",
        "Adresy URL zdjęcia (x,y,z...)",
        "Tekst alternatywny dla zdjęć (x,y,z...)", #filler
        "Usuń istniejące zdjęcia (0 = Nie, 1 = Tak)",
        "Cecha(Nazwa:Wartość:Pozycja:Indywidualne)", #filler
        "Dostępne tylko online (0 = Nie, 1 = Tak)",
        "Stan:"
    ])
    
    for idx, item in enumerate(data.values()):
        row = []


        #categories = ','.join([' '.join([clean_name(y) for y in x.split(' ')]) for x in set(item["category"].split('/'))])
        categories = clean_catpath(item["category"])
        categories = "/".join([clean_name(x) for x in categories.split("/")])


        if(not item["without_discount_price"]):
            price = item["price"]
            discount = ""
        else:
            price = item["without_discount_price"]
            discount = round(float(price.replace(",",".")) - float(item["price"].replace(",",".")), 2)

        photos = ','.join(item["photos_urls"])

        # Te wszystkie None są po to żeby kolejność kolumn w prestashopie sie zgadzała
        # Można ich nie dawać ale wtedy trzeba manualnie/webdriverem wybrać co jest czym
        # a mi się nie chce tego robić
        
        row.append(idx+1) #ID
        row.append(1) #Aktywny
        row.append(item["name"]) #Nazwa
        row.append(categories) #Kategoria
        row.append(price) #Cena (netto)
        row.append(1)
        row.append(None)
        row.append(1 if discount != "" else 0) #W sprzedaży
        row.append(discount) #Wartość rabatu
        row.append(None)
        row.append(None)
        row.append(None)
        row.append(item["code"]) # Indeks #
        row.append(None)
        row.append(None)
        row.append(None)
        row.append(None)
        row.append(None)
        row.append(None)
        row.append(None)
        row.append(None)
        row.append(None)
        row.append(None)
        row.append(None)
        row.append(None)
        row.append(None)
        row.append(random.randint(10,70)) #Ilość
        row.append(1) #Mininalna Ilość
        row.append(5) #Niski poziom produktów w magazynie
        row.append(None)
        row.append("both") #Widoczność (both -> catalog + search)
        row.append(None)
        row.append(None)
        row.append(None)
        row.append("<p>{0}</p>".format(item['details'][1].replace(';',',').replace('\n','').replace('\"','\''))) #Podsumowanie
        row.append(f"<p>{item['details'][0]}</p>") #Opis
        row.append(None)
        row.append(None)
        row.append(None)
        row.append(None)
        row.append(None)
        row.append("Dostępny") # Etykieta w magazynie
        row.append("Niedostępny") # Etykieta backorder
        row.append(1) # Dostępny do zamówienia
        row.append(None)
        row.append(None)
        row.append(1) # Pokaż cenę
        #row.append(photos) # Zdjęcia

        # Tbh, to reszta tych pól z excela wydaje się zbędna i raczej nie trzeba ich mieć
        # Może ktoś inny dodać reszte jeśli bedą potrzebne

        # row.append(None) #ZDJECIA KIEDY ZDJECIA NIE DZIALAJĄ
        # row.append(None)
        # row.append(0) # Usuń isteniejące zdjęcia
        # row.append(None)
        # row.append(0) # Dostęp tylk online
        # row.append("new") # Stan
        

        # Stopper po 50 produktach bo to strasznie długo sie ładuje jak dam całą baze
        # if(idx == 50):
        #     break


        writer.writerow(row)

with open('data_category.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=';',quoting=csv.QUOTE_NONNUMERIC,escapechar='$')

    writer.writerow([
        "ID",
        "Aktywny (0 lub 1)",
        "Nazwa*",
        "Kategoria nadrzędna",
        "Główna kategoria (0/1)",
    ])

    category_set = set()
    id_counter = 3 # ID, 1 i 2 to root i homepage (lub odwrotnie idk)

    def isUnique(w):
        global category_set
        if w not in category_set:
            category_set.add(w)
            return True
        else:
            return False
    
    def write_cat(word):
        global writer, id_counter

        parent, child = word.split("/")
        if parent == child:
            return

        row = []

        row.append(id_counter) # ID, 1 i 2 to root i homepage (lub odwrotnie idk)
        row.append(1) # Aktywny
        row.append(child) # Nazwa
        row.append(parent) # Kat. Nadrzędna
        row.append(0) # Główna kategoria

        writer.writerow(row)

        id_counter += 1

    for idx, item in enumerate(data.values()):
        cats = item["category"]
        
        cats = clean_catpath(cats)

        cats = [clean_name(x) for x in cats.split("/")]
        word = "/"+cats[0]
        if isUnique(word):
            write_cat(word)


        for i in range(len(cats)-1):
            word = cats[i]+"/"+cats[i+1]  
            if isUnique(word):
                write_cat(word)

    



with open('data_combination.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=';',quoting=csv.QUOTE_NONNUMERIC,escapechar='$')

    writer.writerow([
        "Identyfikator Produktu (ID)",
        "Indeks produktu", #filler
        "Atrybut (Nazwa:Typ:Pozycja)*",
        "Wartość (Wartość:Pozycja)*",
        "Identyfikator dostawcy", #filler
        "Indeks", #filler
        "kod EAN13", #filler
        "Kod kreskowy UPC", #filler
        "MPN", #filler
        "Koszt własny", #filler
        "Wpływ na cenę", #filler
        "Podatek ekologiczny", #filler
        "Ilość"
    ])

    def write_size(idx, attr, val):
        global writer
        row = [idx, None, attr, val, None, None, None, None, None, None, None, None, random.randint(10,50)]
        writer.writerow(row)

    for idx, item in enumerate(data.values()):
        sizes = item["size"]

        for size in sizes:
            size = size.split(" ")[0]
            if size == "Rozmiar":
                write_size(idx+1, "", "")
                continue
            write_size(idx+1, "Rozmiar:select:1", size)