#Imports
from bs4 import BeautifulSoup
import requests

#Select RSS Feeds
xml_links = ['http://www.cnbc.com/id/19746125/device/rss/rss.xml', 
'https://fortune.com/feed', 
'https://www.musicbusinessworldwide.com/feed', 
'https://finance.yahoo.com/news/rssindex', 
'https://economictimes.indiatimes.com/rssfeedsdefault.cms', 
'https://www.businesstravelnews.com/rss/business-travel-news',
'https://www.business-live.co.uk/business/?service=rss',
'https://www.ibtimes.com.au/rss'
'https://www.business-standard.com/rss/home_page_top_stories.rss'
'http://rss.cnn.com/rss/money_topstories.rss'
'http://rss.baystreet.ca/'
'http://feeds.feedburner.com/morningstar/glkd'
'https://archive.canadianbusiness.com/business-news/feed/'
'https://www.investing.com/rss/news.rss'
'https://www.financialexpress.com/feed/'
'https://seekingalpha.com/market_currents.xml'
'https://financialpost.com/feed'
'https://bmmagazine.co.uk/feed/'
'https://www.insightssuccess.com/feed/']

link_list = []
title_list = []

#Title and Link Parsing
for i in xml_links:
    url = requests.get(i)
    soup = BeautifulSoup(url.content, 'xml')
    items = soup.find_all('item')
    for item in items:
        title = item.title.text
        the_link = item.link.text
        link_list.append(the_link)
        title_list.append(title)