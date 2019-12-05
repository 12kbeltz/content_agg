# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 22:18:53 2019

@author: 12kbe
"""
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import re

# used to clean up image link
def splitter(string):
    listed = re.split('\(|\)',string)
    return listed[1]

def gr_scrape():
    '''scrapes gripped site for data of head articles'''
    driver = webdriver.PhantomJS(executable_path=
        'C:\\Users\\12kbe\\Documents\\Python\\Stuff\\PhantomJs\\bin\\phantomjs')
    driver.get('https://gripped.com/')
    result = driver.execute_script("return document.documentElement.outerHTML")
    driver.quit()
    soup = BeautifulSoup(result,'lxml')

    # narrows down where to search for data
    gr_articles = soup.find_all('div', {'class':['homeslider slick-slide',
                                        'homeslider slick-slide slick-active']})

    gr_data = {}
    images = []
    links = []
    titles = []

    # scrapes for the specific data and adds to lists above
    for article in gr_articles:
        images.append(splitter(article.attrs['style']))
        
        title_links = article.find('a')
        titles.append(title_links.attrs['title'])
        links.append(title_links.attrs['href'])

    # cobines lists into a single dict that is returned
    gr_data['images'] = images
    gr_data['links'] = links
    gr_data['titles'] = titles

    return gr_data