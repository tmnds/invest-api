import requests
import json
from bs4 import BeautifulSoup


#headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; i64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
headers = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
url = 'https://statusinvest.com.br/acoes/'
ticket = 'raiz4'

response = requests.get(url + ticket, headers=headers)

#if response.status_code == '200':
#   print(type(data.json())) 


soup = BeautifulSoup(response.text, 'html.parser')


# print(f'soup.title: {soup.title}')

# strong_all = soup.find_all('strong', 'value')
# test_all = soup.find_all("div", attrs={"title": "Valor atual do ativo"})
ticket_value = soup.find_all(attrs={'title': 'Valor atual do ativo'})
print(f'Ticket Value: {ticket_value[0].find('strong').text}')

dividend_yield = soup.find_all(attrs={'title': 'Dividend'})
print(f'Ticket Value: {dividend_yield}')



# for element in strong_all:
    # print(element.find_all('strong'))

