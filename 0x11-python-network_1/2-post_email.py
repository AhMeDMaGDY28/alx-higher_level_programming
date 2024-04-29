#!/usr/bin/python3
"""a Python script that takes in a URL, sends a request to the URL and
displays the value of the X-Request-Id
variable found in the header of the response."""

import sys
import urllib.parse
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    # Encode the email parameter
    data = urllib.parse.urlencode({"email": email})
    data = data.encode("ascii")  # Data should be bytes
    req = urllib.request.Request(url, data=data, method="POST")

    with urllib.request.urlopen(req) as response:
        # Read the response body and decode it
        resp_body = response.read().decode("utf-8")
        print(resp_body)
