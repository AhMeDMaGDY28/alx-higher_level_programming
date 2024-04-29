#!/usr/bin/python3
"""A Python script that sends a request to a URL and displays the value of the
X-Request-Id variable in the response header."""

from sys import argv
import requests


if __name__ == "__main__":
    # Get the URL from command line arguments
    url = argv[1]

    try:
        # Send a GET request to the URL with a timeout of 1 second
        response = requests.get(url, timeout=1)

        # Check if the response is not None
        if response is not None:
            # Get the headers from the response
            headers = response.headers

            # Check if 'X-Request-Id' is in the headers
            if "X-Request-Id" in headers:
                # Print the value of 'X-Request-Id'
                print(headers["X-Request-Id"])
    except Exception as e:
        # Print any exceptions that occur (e.g., timeout, connection error)
        print("An error occurred:", e)
