# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 10:31:15 2019

@author: 12kbe
"""

import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

# opens Chrome driver to initiate site scripts, pull data and close chrome
driver = webdriver.PhantomJS(executable_path=
        'C:\\Users\\12kbe\\Documents\\Python\\Stuff\\PhantomJs\\bin\\phantomjs')
driver.get('https://www.neice.com/')
results = driver.execute_script("return document.documentElement.outerHTML")
driver.quit()

soup = BeautifulSoup(results,'lxml')

tables = soup.find_all('article')

images = tables.find_all('img')