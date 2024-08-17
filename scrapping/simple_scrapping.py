from bs4 import BeautifulSoup
import requests


url = "https://sisksa.aou.edu.kw/OnlineApplicationOMN/NewApp.aspx"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

info = soup.findAll("span")

for i in info:
    print(i)
