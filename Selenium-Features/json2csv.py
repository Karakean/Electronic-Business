# ODPALAJ ZE ŚRODKA FOLDERU ./Selenium-Features

import json
import csv
import functools
import random

jf = open('data.json')
data = json.load(jf)
jf.close()

with open('data.csv', 'w', newline='') as csvfile:
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

        # To totalnie nie musi byc jednolinijkowiec ale chce to doprawadzić do najbardziej nieczytelnego stanu jak umiem
        categories = ','.join([' '.join([y.replace(',',' &').capitalize() if len(y) > 1 else y.lower() for y in x.split(' ')]) for x in set(item["category"].split('/'))])
        
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

