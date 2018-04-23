from bs4 import BeautifulSoup
import requests 
import os

url = "https://www.ae.com/men-crew-neck-t-shirts/web/s-cat/6470437?cm=sUS-cUSD&catId=cat6470437"
agents = {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}

response = requests.get(url, headers = agents)
#print response.text.encode('utf-8').strip()

soup = BeautifulSoup(response.text, 'html.parser')
all_pics = set()
for val in soup.find_all("img"):
    try:
        for partial_url in val['data-srcset'].strip().split():
            if partial_url[0] == "/":
                all_pics.add("https:" + partial_url)
    except:
        continue
new = []
for url in all_pics:
    if "large" in url:
        new.append(url)
print(len(new))

for url in new:
    if "of" in url:
        new.remove(url)
print(len(new))
        

count = 0
for pic_url in new:
    with open(str(count) + '.png', 'wb') as handle:
        response = requests.get(pic_url, stream=True)
        handle.write(response.content)
    count += 1
    