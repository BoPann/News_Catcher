from bs4 import BeautifulSoup
import requests
import datetime as dt
from googletrans import Translator

URL = "https://www.economist.com/the-world-in-brief" # the news source
LANGUAGE = 'zh-tw' # The language that the news will be translated into


# scrap the news using beautiful soup
response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')
news_names_spans = soup.select("div._gobbet")
news = [new.getText().strip() for new in news_names_spans]

# get the date
today = dt.datetime.now(); 
today = today.strftime("%m-%d-%y")

# write files
translator = Translator()
with open(today, 'w', encoding='utf-8') as file:
    file.write(f'Headlines of today: {today}\n\n')
    n = 1
    for new in news:
        #translate
        translated_news = translator.translate(new, LANGUAGE)
        translated_news = translated_news.text

        #write original version
        file.write(f'{n}. {new} \n')
        #write translation version
        file.write(f'\n{translated_news} \n\n  ***  \n\n')
        n += 1
