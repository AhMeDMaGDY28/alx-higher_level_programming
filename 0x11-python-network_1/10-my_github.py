#!/usr/bin/python3
"""Retrieve GitHub user id using GitHub API"""

from sys import argv
import requests


if __name__ == "__main__":
    # Extract username and password from command line arguments
    username = argv[1]
    password = argv[2]

    try:
        # Send a GET request to GitHub API with Basic Authentication
        response = requests.get(
            "https://api.github.com/user", auth=(username, password), timeout=1
        )

        # Parse the JSON response
        json_response = response.json()

        # Check if the response contains the user id
        if "id" in json_response:
            print(json_response["id"])
        else:
            # Print None if user id is not found in the response
            print("None")
    except requests.exceptions.RequestException as e:
        # Handle request exceptions
        print("An error occurred:", e)
