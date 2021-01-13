#!/usr/bin/env python3
# create a list of strings
vendors = ["*", "**", "***", "****", "*****", "****", "***", "**","*"]
# create a second list of strings
approved_vendors = ["cisco", "juniper", "big_ip"]
# loop across the list called vendors
for x in range(-3,5): #brad
    print("*" * abs(abs(x) - 5))
print("\nOur loop has ended.") # print when loop has finished

