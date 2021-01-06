#!/usr/bin/env python3

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]


hurtMeh= int(input("0: NE Farm \n 1: W Farm \n 2: SE Farm \n")) #allows usr to select inside loop
for plants in farms[hurtMeh]["agriculture"]: #retrieves usr input, input becomes index
    if plants == "carrots":
        print("Just Animals Please")
        continue
    elif plants == "celery":
        print("I said ANIMALS!!")
        continue
    print(plants)
