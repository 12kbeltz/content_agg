# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 11:44:03 2019

@author: 12kbe
"""

from flask import Flask, render_template
from ne_ice_ws import ne_scrape
from uphill_ws import ua_scrape


app = Flask(__name__)

ne_info = ne_scrape()
ua_info = ua_scrape()

@app.route('/')
def hello():
    return render_template('homepage.html',
                           the_title='Homepage',
                           ne_photo0=ne_info['images'][0], ua_photo0=ua_info['images'][0],
                           ne_link0=ne_info['links'][0], ua_link0=ua_info['links'][0],
                           ne_name0=ne_info['titles'][0], ua_name0=ua_info['titles'][0],
                           ne_photo1=ne_info['images'][1],
                           ne_link1=ne_info['links'][1],
                           ne_name1=ne_info['titles'][1],
                           ne_photo2=ne_info['images'][2],
                           ne_link2=ne_info['links'][2],
                           ne_name2=ne_info['titles'][2],
                           ne_photo3=ne_info['images'][3],
                           ne_link3=ne_info['links'][3],
                           ne_name3=ne_info['titles'][3],
                           ne_photo4=ne_info['images'][4],
                           ne_link4=ne_info['links'][4],
                           ne_name4=ne_info['titles'][4])

app.run(debug=True)