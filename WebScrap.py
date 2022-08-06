#Web Scrapping
#Imports
from bs4 import BeautifulSoup
import requests
import index

#Filter Words Selected From Adobe's Product List: https://www.adobe.com/products/catalog.html
filtered_list = []
filtered_title = []
indexer = -1
filter_words_one = ["PDF", "PDF solution", "images", "graphics", "art", "video editing", "film editing", "vector art", "videos", "content", "templates", "cinematic", "cinema", "visual effects", "motion graphics", "photos", "digital storage", "layouts", "user experiences", "design", "prototype", "animation", "web sites", "3D scenes", "3D models", "3D materials", "3D assets", "audio", "copywriting", "editors", "editing", "share", "create", "augmented reality", "sign", "digital workflows", "scan", "customer interactions", "analytics", "eCommerce", "digital commerce", "real-time profiles", "marketing", "digital interactions", "marketing", "test", "optimize", "machine learning", "delivering", "media strategies", "search marketing", "TV advertising", "creative management", "CMS", "customer journey", "customer behavior", "campaign", "content management", "data management", "insights", "personalization", "marketing automation", "lead nurturing", "account-based marketing", "drawing", "painting", "fonts", "color theme", "graphic", "brush", "pattern", "texture", "video files", "showcase", "discover", "creative work", "creative assets", "learning experience", "real-time communication", "eBook", "HTTP streaming", "help policy", "knowledge base content", "printing", "documents", "video studio", "automated publishing", "stream", "stream videos", "technical content", "monetize", "on-demand", "media", "IDE", "automation", "web conferencing", "business content", "money suite", "applications", "color themes"]
filter_words_two = [""]

#Filter
for i in index.link_list:
    url = requests.get(i)
    soup = BeautifulSoup(url.content, 'html.parser')
    items = soup.find_all('p')
    indexer += 1
    for stuff in items:
        item = stuff.text.lower()
        for filterone in filter_words_one:
            if filterone in item:
                for filtertwo in filter_words_two:
                    if filtertwo in item:
                        if i not in filtered_list:
                            filtered_list.append(i)
                        if index.title_list[indexer] not in filtered_title:
                            filtered_title.append(index.title_list[indexer])
                        break

#Printing Results
#print(filtered_list)
#print(filtered_title)