# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 09:11:10 2019

@author: 12kbe
"""

from ne_ice_ws import ne_scrape
from time import time

start = time()
x = ne_scrape()
y = time() - start
print('It takes {} seconds to scrape a website'.format(y))