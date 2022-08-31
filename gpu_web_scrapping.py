from bs4 import BeautifulSoup
import requests

def check_price(no_pages):

    url = 'https://www.newegg.com/Desktop-Graphics-Cards/SubCategory/ID-48?Tid=7709&PageSize=96'
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"}
    page = requests.get(url, headers=headers)
    
    soup1 = BeautifulSoup(page.content, 'html.parser')
    soup2 = BeautifulSoup(soup1.prettify(), 'html.parser')
    
    gfxcards = []
    
    import datetime
    
    for list in soup2.find_all('div', class_='item-container'):
        title = list.find('a', class_='item-title').get_text().replace('\n', '').replace('RADEON', 'Radeon').strip()
        price = list.find('li', class_='price-current').get_text().replace('\n', '').strip().split()
        link = list.find('a')['href']
        shipping = list.find('li', class_='price-ship').get_text().replace('\n', '').strip()
        
        allCards = []
        
        if "GeForce" in title:
            allCards.append("Nvidia")
        elif "Radeon" in title:
            allCards.append("Radeon")
        else:
            allCards.append("Unknown")
        
        allCards.append(title.split()[0])
        
        if "GeForce" in title and 'Ti' not in title:
            allCards.append(title.split("GeForce",1)[1][1:9])
        elif "GeForce" and 'Ti' in title:
            allCards.append(title.split("GeForce",1)[1][1:12])
        elif "Radeon" and 'XT' in title:
            allCards.append(title.split("Radeon",1)[-1][1:11])
        elif 'Radeon' in title and 'XT' not in title:
            allCards.append(title.split("Radeon",1)[1][1:8])
        else:
            allCards.append('Unknown')

        try:
            allCards.append(int(price[1]))
        except:
            allCards.append(0)

        allCards.append(shipping)

        allCards.append(link)
        
        gfxcards.append(allCards)

    return gfxcards