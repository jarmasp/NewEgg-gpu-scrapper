from csv import writer
import pandas as pd
from gpu_web_scrapping import *
1
no_pages = int(input('how many pages do you want to scrape?: '))

results = []
for i in range(1, no_pages+1): 
    results.append(check_price(i))

unpack = lambda l: [item for sublist in l for item in sublist]

df = pd.DataFrame(unpack(results),columns=['Manufacturer','Brand','Model','Price', 'Shipping', 'Link'])
df.to_csv('Graphics card price.csv', index=False, encoding='utf-8')