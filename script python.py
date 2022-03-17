# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 14:17:27 2022

@author: facu_
"""

from pip._vendor import requests

site_id='MLA'
seller_id = int(input("seller_id: "))
    
fil_1a="results";
fil_2a="id";
fil_2b="title";
fil_2c="category_id";
fil_2d="domain_id";
url=f"https://api.mercadolibre.com/sites/{site_id}/search?seller_id={seller_id}";
nombre_archivo= f"MeLiChallenge.log";


try:
    results=requests.get(url)
    res_json=results.json()
    res_interes=res_json[fil_1a];

    with open(nombre_archivo,"wt") as file:
            for item in res_interes: 
                item_dat= [f"ID: {item[fil_2a]}",f"\nTitulo:{item[fil_2b]}",f"\nID de la categoria: {item[fil_2c]}",f"\nNombre de la categoria: {item[fil_2d]}"]
                file.writelines(item_dat)
                file.write("\n");
            print("El archivo: "+ nombre_archivo + " se ha creado correctamente");
                           
except:
    print("error al guardar el archivo");