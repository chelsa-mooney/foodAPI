#!/usr/bin/env python3
#keys
import requests
from pprint import pprint
import spoonacular as spoon
apiKey = spoon.API("735810a590ed41ad81ca2a1ccbcd3703")

print("Hello!")
ingredients = input("Feed me a list of ingredients! ")

headers = {
    'content-type': "application/json",
    }
query = ingredients
response = apiKey.search_recipes_by_ingredients(ingredients)
pprint(response.json())
print("Sound yummy? Yes! No, give me another recipe. ")


#response = requests.get("https://api.spoonacular.com/recipes/complexSearch?apiKey=735810a590ed41ad81ca2a1ccbcd3703")
#data = response.json()
#print(data)