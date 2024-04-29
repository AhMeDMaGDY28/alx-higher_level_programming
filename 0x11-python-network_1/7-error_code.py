#!/usr/bin/python3
"""A Python script that sends a request to a URL and displays the body of the response,
handling HTTP errors if they occur."""

from sys import argv
import requests

if __name__ == "__main__":
    # Get the URL from command line arguments
    the_url = argv[1]

    try:
        # Send a GET request to the URL
        response = requests.get(the_url)

        # Check if the HTTP status code is greater than or equal to 400
        if response.status_code >= 400:
            # Print the error code if an error occurs
            print("Error code:", response.status_code)
        else:
            # Print the body of the response
            print(response.text)
    except Exception as e:
        # Print any exceptions that occur during the request
        print("An error occurred:", e)
