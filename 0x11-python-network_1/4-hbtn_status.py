#!/usr/bin/python3
"""A Python script that fetches https://alx-intranet.hbtn.io/status
using the requests package."""

import requests

if __name__ == "__main__":
    # Define the URL
    the_url = "https://alx-intranet.hbtn.io/status"

    # Send a GET request to the URL
    respon = requests.get(the_url)

    # Extract the text content of the response
    content = respon.text

    # Print the body response with formatted output
    print("Body response:")
    print("\t- type:", type(content))
    print("\t- content:", content)
