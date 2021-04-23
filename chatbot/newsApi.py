from newsapi import NewsApiClient
from pandas import json_normalize

# Init
newsapi = NewsApiClient(api_key='1fa3d77b9ae7460c833ef91fe447eca4')


def top_headlines():
    country = "gb"
    category = "technology"
    top_titles = newsapi.get_top_headlines(category=category,
                                           language='en', country=country)
    top_titles = json_normalize(top_titles['articles'])
    new_df = top_titles[["title", "url"]]
    dic = new_df.set_index('title')['url'].to_dict()
    return dic
