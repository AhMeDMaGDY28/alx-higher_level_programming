#!/usr/bin/python3
"""a Python script that takes in a URL, sends a request to the URL and
displays the value of the X-Request-Id
variable found in the header of the response."""

from sys import argv
import urllib.parse
import urllib.request


if __name__ == "__main__":
    URL = argv[1]
    email = argv[2]
    # Encode the email parameter
    data = urllib.parse.urlencode({"email": email})
    data = data.encode("utf-8")
    request = urllib.request.Request(URL, data)

    with urllib.request.urlopen(request) as respon:
        # Read the response body and decode it
        body_resp = respon.read()
        print(body_resp.decode("utf-8"))
