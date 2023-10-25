import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://books.toscrape.com/"


def get_html_data(url):
    r = requests.get(url)
    if r.status_code == 200: #try except
        print("web can be accessed")
    result = r.text #string
    return result


def save_html(html_data, filename):
    with open(f"{filename}.html", "w") as html:
        html.writelines(html_data)


def scraping(cards):
    list_result = []
    for card in cards:
        title = card.find("h3").find("a")['title']
        price = card.find("p", class_="price_color").get_text().replace("Â", "")
        value_dict = {"title" : title, "price" : price}
        list_result.append(value_dict)
    return list_result


def save_image_to_jpg(image_data, file_name):
    """
    Save image data to a JPG file locally.
    
    Parameters:
        image_data (bytes): Image data in binary format.
        file_name (str): Name of the output JPG file.
    
    Returns:
        bool: True if the image was successfully saved, False otherwise.
    """
    try:
        with open(file_name, "wb") as img_file:
            img_file.write(image_data)
        print(f"Image successfully saved as {file_name}")
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

html_result = get_html_data(url)
save_html(html_result, "output")
soup = BeautifulSoup(html_result, features="html.parser") #lxml dan html.parser
cards = soup.find_all("li", class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")
result = scraping(cards)
df = pd.DataFrame(result)
print(df)
df.to_excel("output.xlsx", index=False)
"""
1. Fetching data or HTML nya dari website https://books.toscrape.com/
1a. Simpen hasilnya kesebuah file html lokal
2. Kita akan mulai coba parsingnya
3. simpan hasil parsingnya ke xlsx

Tugas :
1. scraping href
2. scraping gambar
3. scraping status(in stock or out of stock)
4. scraping star nya (mungkin clue, if star=One, maka bintang satu, dst)
"""

link_img = "../../../media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg".replace("../../../", "")
final_link = f"https://books.toscrape.com/{link_img}"
print(final_link)
"https://books.toscrape.com + /media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg"