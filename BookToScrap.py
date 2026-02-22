import csv
import requests as rq
from bs4 import BeautifulSoup as bs
word_to_int_map = {
        "Zero": '0/5', "One": '1/5', "Two": '2/5', "Three": '3/5', "Four": '4/5',
        "Five": '5/5'
}
header = {"User-Agent":
 "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
with open ('book.csv',"wt") as file:
    writer = csv.writer(file)
    writer.writerow(['Title','Price(Â£)','Rate'])

    try:
        for page in range(1,51):
            if page == 0:
                url = 'https://books.toscrape.com'
            else:
                url = f'https://books.toscrape.com/catalogue/page-{page}.html'

            r = rq.get(url,headers=header,timeout=10)
            soup = bs(r.text,"html.parser")
            books = soup.find_all("article", class_ = "product_pod")
            for book in books:
                title = book.h3.a["title"]
                price = book.find("p",class_="price_color").text
                price = price.replace('Â£','')
                rate = book.find("p", class_="star-rating")
                rate =word_to_int_map[rate["class"][1]]
                writer.writerow([title, price, rate])
            print(f"{page}/50 page is completed")
    except:
        print('error')
    finally:
        print('scraping done, csv file is created')