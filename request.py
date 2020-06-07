# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 12:35:41 2020

@author: gaurav sahani
"""


import requests

url = 'http://localhost:5000/irisflowerclassprediction-api'
r = requests.post(url,json={'SepalLengthCm':4, 'SepalWidthCm':3, 'PetalLengthCm':6, 'PetalWidthCm':5 })

print(r.json())