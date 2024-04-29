#!/usr/bin/python3
"""A Python script that takes in a URL, sends a request to the URL, and
displays the body of the response (decoded in utf-8)."""

import urllib.error
import urllib.request
from sys import argv

if __name__ == "__main__":
    # Get URL from command line arguments
    url = argv[1]

    # Create a request object
    request = urllib.request.Request(url)

    try:
        # Open the URL and handle the response
        with urllib.request.urlopen(request) as response:
            # Read the body of the response
            body_response = response.read()
            # Decode the body to utf-8 and print
            print(body_response.decode("utf-8"))
    except urllib.error.HTTPError as error:
        # If an HTTP error occurs, print the error code
        print("Error code: {}".format(error.code))
