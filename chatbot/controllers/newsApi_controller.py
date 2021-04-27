from newsapi import NewsApiClient
from pandas import json_normalize


def top_headlines():
    newsapi = NewsApiClient(api_key='1fa3d77b9ae7460c833ef91fe447eca4')  # generated my own api key by registering
    country = "gb"
    category = "technology"
    top_titles = newsapi.get_top_headlines(category=category,
                                           language='en', country=country)
    top_titles = json_normalize(top_titles['articles'])  # top_headlines organised in json format
    print(top_titles)
    new_df = top_titles[["title", "url"]]  # grabbing each top titles' title and urls
    dic = new_df.set_index('title')['url'].to_dict()
    # creating dictionary with the value being the url and the title as the key
    return dic
