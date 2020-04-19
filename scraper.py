import requests
from bs4 import BeautifulSoup
import smtplib

val = print('enter url:')

URL= input()

val2 = print('enter email:')
email = input()

# val3 = print('enter target price:')
# tprice = input()

# URL = 'https://www.amazon.com/Starbucks-French-Single-Coffee-Brewers/dp/B0788C3NGD/ref=sr_1_6?crid=1EXTF9F8VODAY&keywords=french+roast+coffee+k+cups&qid=1579977609&sprefix=french+roa%2Caps%2C190&sr=8-6'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}


def check_price():
    page = requests.get(URL, headers=headers)

    soup1 = BeautifulSoup(page.content, 'html.parser')
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    title = soup2.find(id="productTitle")
    price = soup2.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[1:5])

    if(converted_price < 22):
        send_mail()


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('azpricetrak@gmail.com', 'iyjmwqvuhcctgvyk')

    subject = 'Amazon Price Alert!'
    body = 'The price on your item has fallen! please follow this link:', URL

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'azpricetrak@gmail.com',
        email,
        msg
    )

    server.quit()

check_price()
