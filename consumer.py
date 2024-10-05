import requests
from bs4 import BeautifulSoup

source = "https://www.google.com/finance/quote/"
ticket = "RAIZ4:BVMF"
window = "window=MAX"

url = source + ticket + "?" + window

print(url)

#https://www.google.com/finance/quote/RAIZ4:BVMF?window=5D 
#https://www.google.com/finance/quote/ETH-USD?hl=pt

headers = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
response = requests.get(url, headers=headers) 

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    # print(soup.prettify())



    # with open("arquivo.txt", 'a') as f:
    #     f.write(data)



# Valor do dia na <div soy-skip ssk="6:m3t7je"
