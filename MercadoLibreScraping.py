from bs4 import BeautifulSoup
import requests
import pandas as pd

#Hola Gente de GIT-HUB"

Enlace = 'https://listado.mercadolibre.com.mx/telefonos-celulares#D[A:telefonos%20celulares]'
page = requests.get(Enlace)
soup = BeautifulSoup(page.content, 'html.parser')

#Celulares
Celu = soup.find_all('h2', class_='ui-search-item__title')
Celulares = []
count = 0
for i in Celu:
    if count < 30:
        Celulares.append(i.text)
    else:
        break
    count += 1
#Precios
Cos = soup.find_all('span', class_='price-tag-fraction')
Costos = []
count = 0
for i in Cos:
    if count < 30:
        Costos.append(i.text)
    else:
        break
    count += 1

df = pd.DataFrame({'Nombre': Celulares, 'Precio': Costos}, index = list(range(1,31)))
print(df)
df.to_csv('Precios Totales.csv', index=False)
