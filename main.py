import requests
from bs4 import BeautifulSoup
import smtplib
# Add the os and dotenv modules
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

url='https://www.amazon.com/AKASUKI-Bedroom-Dimmable-Charging-Included/dp/B0D12JQHZF/ref=sr_1_13_sspa?crid=7I5IVXLA0YWE&dib=eyJ2IjoiMSJ9.hMRjb7dErktgK2fMTItSWZ0sjyOKnpS1Qs07y11agCZoeye85atHiwJDx9QP0Woz6fmtYS6XwNvdyzBE3mKuHAbNefwCX1bTpZYiRjslzR_IZmXebeBhok_1Q8Z-KQJ1MA9_lhCtJmRAxI7lWrSdYDdsc1oIv1X2h4mJeJTZmmgMitbGXRXbMctma92EfgXcCuZhmoDAJ_IYHGNJ5QxesXIGzRjISutonvcmZANKOT-SKhBLDScul7qj-uubdY_9Wr57MwNLdxnkfsj_E5NasIyq8pR2bmm-x0dYnYSWgRA.999EoXZ3UY5JtLuBe74mc5LA0juvu0K4T4HuqZwY3c8&dib_tag=se&keywords=lamps&qid=1768127057&s=hi&sprefix=lamp%2Ctools%2C362&sr=1-13-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9tdGY&th=1'
response=requests.get(url,headers={'User-Agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36","Accept-Language": "en-US,en;q=0.9"})
soup=BeautifulSoup(response.content,'html.parser')
with open('html.txt','w',encoding="utf-8") as file:
    file.write(soup.prettify())

price = soup.find(class_="a-offscreen").get_text()
price_without_currency=price.replace('INR','').replace(',','')
price_as_float = float(price_without_currency)
# print(price_as_float)


title = soup.find(name="title").get_text().strip('- Amazon.com')
# print(title)

#for email
buy_Price=2000
if price_as_float<buy_Price:
    message=f"Price drop detected 📉\n {title} is now available for {price}."
    with smtplib.SMTP(os.environ['SMTP_ADDRESS'], port=587) as connection:
        connection.starttls()
        result = connection.login(os.environ['USER_EMAIL'],os.environ['Your_Password'])
        connection.sendmail(
            from_addr=os.environ['USER_EMAIL'],
            to_addrs=os.environ['USER_EMAIL'],
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
        )