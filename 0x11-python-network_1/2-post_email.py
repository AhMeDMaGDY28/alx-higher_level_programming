#!/usr/bin/python3
"""A Python script that sends a POST
request with an email parameter to a given URL
and displays the body of the response."""

from sys import argv
import urllib.parse
import urllib.request


if __name__ == "__main__":
    # Extract the email and URL from command line arguments
    email = argv[2]
    url = argv[1]

    # Define the parameters to be sent in the POST request
    params = {"email": email}

    # Encode the parameters
    data = urllib.parse.urlencode(params)
    data = data.encode("utf-8")

    # Create a POST request with the encoded data
    request = urllib.request.Request(url, data)

    # Send the request and handle the response
    with urllib.request.urlopen(request) as response:
        # Read the body of the response and decode it
        body_response = response.read().decode("utf-8")

        # Print the body of the response
        print(body_response)
