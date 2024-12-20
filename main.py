import requests
from bs4 import BeautifulSoup
import json
URL="https://quotes.toscrape.com/"
response=requests.get(URL)
if response.status_code !=200:
    print("Ошибка при запросе {response.status_code} ")
    exit()
soup = BeautifulSoup(response.content, "html.parser")
quotes = []
for quote in soup.find_all("div", class_="quote"):
    text_quote = quote.find("span", class_="text").get_text()
    authors_quote = quote.find("small", class_="author").get_text()
    quotes.append({"quote": text_quote, "author": authors_quote})


def print_quotes(quotes):#вывод цитат
    for i, quote in enumerate(quotes, 1):
        print(f'{i}. Quote: {quote["quote"]}; Author: {quote["author"]};')

print_quotes(quotes)
def save(quotes,file="data.json"):
     with open(file,"w",encoding="utf-8")as file_data:
        json.dump(quotes, file_data, ensure_ascii=False, indent=4)

save(quotes)
html_inf="""
 <html>
    <head>
        <title>Список цитат</title>
         <style>
            
            p {
                border: 2px solid rgb(80, 141, 39);
                padding: 30px;
            } 
         
            body {
                color: #2f4d04;
            }
            table {
                background: #99a766;
            }
            th, td {
                padding: 55px;
                border: 1.5px solid #d6e0c7;
                text-align: left;
            }
            th {
                background-color: #457731;
                color: #111808;
                padding: 30px;
                 font-size: 20px;
            }
            h1 {
                text-align: center;
                margin-bottom: 50px;
            }
            p {
                text-align: center;
                margin-top: 40px;
            }
            a {
                color: #537a13;
                text-decoration: none;
            }
        </style>
    </head>
    <body>
        <div>
            <h1><p>Цитаты</p></h1>

           
            <table>
            
                <tr>
                    
                    <th>№ цитаты</th>
                    <th>Цитата</th>
                    <th>Автор</th>
                </tr>
                
            
            <h2><i><a href="http://quotes.toscrape.com/">Источник: Quotes to Scrape </a></i></h2>
            
        </div>
    </body>
    
    """

    # Добавление цитат в таблицу
for i, quote in enumerate(quotes, 1):
    html_inf+= f'''
    <tr>
        <td><h3>{i}</h3></td>
        <td><h3>{quote["quote"]}</h3></td>
        <td><h3>{quote["author"]}</h3></td>
    </tr>
    '''
    html_inf += '''
</html>
    '''

with open('index.html', 'w', encoding='utf-8') as sec_file:
    sec_file.write(html_inf)  # записываем сгенерированный HTML-код в файл  

