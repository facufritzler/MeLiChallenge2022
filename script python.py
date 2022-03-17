# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 13:56:35 2022

@author: facu_
"""

import requests


SITE_ID='MLA'
SELLER_ID = int(input("SELLER_ID: "))


req = requests.get(f"https://api.mercadolibre.com/sites/{SITE_ID}/search?seller_id={SELLER_ID}")

info = req.json()
items = info['results']


print('Procesando, por favor, espere.')



with open("MeLiChallenge.LOG", 'w') as f:
    for item in items:
        itemID = item['id']
        title = item['title']
        category_id = item['category_id']

        req = requests.get(f"https://api.mercadolibre.com/categories/{category_id}")
        info = req.json()
        
        category_name = info['name']

        
        print(itemID, title, category_id, category_name, file=f)
        

print('Se finalizo el procesamiento')		