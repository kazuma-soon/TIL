# https://axross-recipe.com/recipes/54#overview
import re
from bs4 import BeautifulSoup
import requests
import time
import csv
import os

url_list = ['https://suumo.jp/jj/chintai/ichiran/FR301FC001/?ar=030&bs=040&ta=13&sc=13101&sc=13102&sc=13103&sc=13104&sc=13105&sc=13113&cb=0.0&ct=9999999&et=9999999&cn=9999999&mb=0&mt=9999999&shkr1=03&shkr2=03&shkr3=03&shkr4=03&fw2=&srch_navi=1',]
save_dir = './data'
output_path_list = ['center.csv',]
num_pages = 3

os.makedirs(save_dir)
for (url, output_path) in zip(url_list, output_path_list):
    urls = []
    
    # ページングに合わせたURLをリストとして作成
    for page in range(1, num_pages+1):
        url_page = url + '&page={}'.format(page)
        urls.append(url_page)
    print('number of urls is {}'.format(len(urls)))

    f = open('{}/{}'.format(save_dir, output_path), 'a')
    for url in urls:
        print('get data of url({})'.format(url))
        new_list = []
        result = requests.get(url)  # サーバからHTML、XMLなどの情報を取得
        c = result.content  # parseが必要なぐちゃぐちゃデータを取得
        soup = BeautifulSoup(c, "html.parser") # これでfindが使用できる
        
        summary = soup.find("div",{'id':'js-bukkenList'}) # リスト全体
        apartments = summary.find_all("div",{'class':'cassetteitem'}) # 個々の物件
        for apart in apartments:
            room_number = len(apart.find_all('tbody'))
            name = apart.find("div",{'class':'cassetteitem_content-title'}).text
            address = apart.find("li", {'class':"cassetteitem_detail-col1"}).text
            age_and_height = apart.find('li', class_='cassetteitem_detail-col3')
            age = age_and_height('div')[0].text
            height = age_and_height('div')[1].text
            money = apart.find_all("span", {'class':"cassetteitem_other-emphasis ui-text--bold"})
            madori = apart.find_all("span", {'class':"cassetteitem_madori"})
            menseki = apart.find_all("span", {'class':"cassetteitem_menseki"})
            floor = apart.find_all("td")

            for i in range(room_number):
                write_list = [name, address, age, height, money[i].text, madori[i].text, menseki[i].text, floor[2+i*9].text.replace('\t', '').replace('\r','').replace('\n', '')]
                writer = csv.writer(f)
                writer.writerow(write_list)
        time.sleep(5)