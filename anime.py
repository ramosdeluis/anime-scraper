import requests
import csv
from bs4 import BeautifulSoup
from time import sleep


def get_anime_ranking(how_muchu: int):

    my_list = [50 * (num // 50) for num in range(how_muchu)]
    my_list = sorted(list(set(my_list)))

    all_data = []

    for num in my_list:

        url = f'https://myanimelist.net/topanime.php?limit={num}'

        response = requests.get(url)

        soup = BeautifulSoup(response.content, 'html.parser')

        data = soup.select('.ranking-list .hoverinfo_trigger.fl-l.fs14.fw-b.anime_ranking_h3 a')
        ranking = soup.select('.ranking-list .js-top-ranking-score-col.di-ib.al span')

        for num, ele in enumerate(data):
            all_data.append([ele, ranking[num]])

        sleep(0.5)


    headers = ['ranking', 'name', 'score', 'link']

    with open('anime_ranking.csv', 'w', newline='') as file:

        csvwriter = csv.writer(file)

        csvwriter.writerow(headers)

        for num, d in enumerate(all_data):
            csvwriter.writerow([f'{num + 1}', d[0].text, d[1].text, d[0].get('href')])


        
         

get_anime_ranking(10000)
