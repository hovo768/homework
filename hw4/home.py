from PIL import Image
import requests
from datetime import *
from decimal import *

#1

myimage = Image.open(r'C:\Users\Hovo768\Desktop\01.png')
myimage.load()
myimage_2 = Image.open(r'C:\Users\Hovo768\Desktop\02.png')
myimage_2.load()


#2

# def currency_rates(mon):
#     money = mon.upper()
#     response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text
#
#     if money not in response:
#         return None
#
#     rub = response[response.find('<Value>', response.find(mon)) + 7:response.find('</Value>', response.find(mon))]
#     day_raw = response[response.find('Date="') + 6:response.find('"', response.find('Date="') + 6)].split('.')
#     day, month, year = map(int, day_raw)
#     return f"{Decimal(rub.replace(',', '.'))}, {datetime(day=day, month=month, year=year)}"




#3
import utils
print(utils.currency_rates('EUR'))


#4
import sys
print(utils.currency_rates(sys.argv[1]))

