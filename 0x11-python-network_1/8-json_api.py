#!/usr/bin/python3
"""A Python script that sends a POST request to search for a user
based on a given letter."""

from sys import argv
import requests


if __name__ == "__main__":
    # Check if an argument is provided, otherwise set q to an empty string
    if len(argv) == 1:
        q = ""
    else:
        q = argv[1]

    # Create a dictionary with the query parameter
    payload = {"q": q}

    # Define the URL for the POST request
    the_URL = "http://0.0.0.0:5000/search_user"

    try:
        # Send a POST request with the provided query parameter
        response = requests.post(the_URL, data=payload)

        try:
            # Attempt to parse the response as JSON
            json_response = response.json()

            # Check if the JSON response is empty
            if len(json_response) == 0:
                print("No result")
            else:
                # Extract and print the id and name from the JSON response
                print("[{}] {}".format(
                    json_response["id"], json_response["name"]))
        except ValueError:
            # Print an error message if the response is not valid JSON
            print("Not a valid JSON")
    except Exception as e:
        # Print any exceptions that occur during the request
        print("An error occurred:", e)
