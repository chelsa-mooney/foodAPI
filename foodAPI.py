#!/usr/bin/env python3
#keys
import requests
from pprint import pprint
import spoonacular as spoon
apiKey = spoon.API("735810a590ed41ad81ca2a1ccbcd3703")

headers = {
    'content-type': "application/json",
    }

#ingredients list
food_list = []

#asks for user input    
print("Hello!")
ingredients = input("Feed me a list of ingredients! ")

#API recipe search
def new_func(apiKey, ingredients):
    query = ingredients
    response = apiKey.search_recipes_by_ingredients(ingredients)
    pprint(response.json())

new_func(apiKey, ingredients)
prompt1 = input("Sound yummy? Yes! No, give me another recipe. ").lower()
if prompt1 == "yes":
    food_list.append(ingredients)
else: 
    ingredients = input("Feed me a list of ingredients! ")
    new_func(apiKey, ingredients)

print(food_list)

#grocery store map of products
def map_ingredients_to_grocery_products(food_list, servings):
    query = "food/ingredients/map"
    response = apiKey.map_ingredients_to_grocery_products(food_list)
map_ingredients_to_grocery_products(food_list)