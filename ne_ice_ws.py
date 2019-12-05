# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 11:01:59 2019

@author: 12kbe
"""

import requests
from bs4 import BeautifulSoup

def ne_scrape():
    '''scrapes neice site for data of head articles'''
    result = requests.get('https://www.neice.com/')
    src = result.content
    soup = BeautifulSoup(src,'lxml')

    # narrows down where to search for data
    ne_context = soup.find_all('div', {'class':'avia-content-slider-inner'})
    ne_articles = ne_context[0].find_all('a', {'class':'slide-image'})
    ne_titles = soup.find_all('div',
                              {'class':'slide-entry-excerpt entry-content'})

    ne_data = {}
    images = []
    links = []
    titles = []

    # scrapes for the specific data and adds to lists above
    for article in ne_articles:
        links.append(article.attrs['href'])

        title_image = article.find('img')
        images.append(title_image.attrs['src'])
    
    for title in ne_titles:
        titles.append(title.string)
        
    # cobines lists into a single dict that is returned
    ne_data['images'] = images
    ne_data['links'] = links
    ne_data['titles'] = titles
    
    return ne_data


