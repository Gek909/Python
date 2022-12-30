import requests
from bs4 import BeautifulSoup



def get_currency_rate(currency_name):
    url = f'https://www.moex.com/ru/derivatives/currency-rate.aspx?currency={currency_name}'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    mass = soup.find_all(class_="col-md-36 margin-tb-10")
    print(mass)
    string = str(soup.find_all(class_="col-md-36 margin-tb-10"))
    string = string[string.find('<b>')+3:string.find('</span>'):]
    for x, y in (",", "."), ("</b>",""), ("  ", " "):
        string = string.replace(x, y)
    return string