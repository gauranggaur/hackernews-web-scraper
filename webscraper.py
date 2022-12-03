import requests                # to get data
from bs4 import BeautifulSoup  # to cleanup data
import pprint                  # to print output in a neater way

response = requests.get('https://news.ycombinator.com/')

soup = BeautifulSoup(response.text, 'html.parser')

links = soup.select('.titleline')
subtext = soup.select('.subtext')

def custom_hackernews(links, subtext):
    hackernews = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.find('a').get('href')
        score = subtext[idx].select('.score')
        if len(score):
            votes = int(score[0].getText().replace(' points', ''))
            if votes > 99:
                hackernews.append({'title': title, 'link': href, 'votes': votes})
    sorted_list = sorted(hackernews, key=lambda k: k['votes'], reverse=True)
    return sorted_list

pprint.pprint(custom_hackernews(links, subtext))