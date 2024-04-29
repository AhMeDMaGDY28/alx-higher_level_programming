#!/usr/bin/python3
"""A Python script that sends a POST request with an email parameter to a URL
and displays the body of the response."""

import requests
from sys import argv

if __name__ == "__main__":
    # Get the URL and email address from command line arguments
    url = argv[1]
    email = argv[2]

    # Create a dictionary with the email as a parameter
    data = {"email": email}

    try:
        # Send a POST request to the URL with the email parameter
        response = requests.post(url, data=data)

        # Get the body of the response
        response_body = response.text

        # Print the body of the response
        print(response_body)
    except Exception as e:
        # Print any exceptions that occur during the request
        print("An error occurred:", e)
