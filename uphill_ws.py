# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 16:49:55 2019

@author: 12kbe
"""
import requests
from bs4 import BeautifulSoup

def ua_scrape():
    '''scrapes uphill athletes site for data of head articles'''
    result = requests.get('https://www.uphillathlete.com/')
    src = result.content
    soup = BeautifulSoup(src,'lxml')

    # narrows down where to search for data
    ua_context = soup.find_all('ul', {'class':'slides'})
    ua_articles = ua_context[0].find_all('a', {'class':'image-link'})

    ua_data = {}
    images = []
    links = []
    titles = []

    # scrapes for the specific data and adds to lists above
    for article in ua_articles:
        links.append(article.attrs['href'])
        
        title_image = article.find('img')
        titles.append(title_image.attrs['alt'])
        images.append(title_image.attrs['src'])

    # cobines lists into a single dict that is returned
    ua_data['images'] = images
    ua_data['links'] = links
    ua_data['titles'] = titles

    return ua_data