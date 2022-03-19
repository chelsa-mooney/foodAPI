#!/usr/bin/env python3
#keys
import requests
import spoonacular as spoon
apiKey = spoon.API("735810a590ed41ad81ca2a1ccbcd3703")

#print("Hello!")
#ingredients = input("Feed me a list of ingredients! ")


#response = requests.get("https://api.spoonacular.com/recipes/complexSearch?apiKey=735810a590ed41ad81ca2a1ccbcd3703")
#data = response.json()
#print(data)

headers = {
    'content-type': "application/json",
    }

response = apiKey.get_a_random_food_joke()
data = response.json()
print(data['text'])
