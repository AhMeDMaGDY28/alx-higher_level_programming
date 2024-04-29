#!/usr/bin/python3
"""a Python script that takes in a URL, sends a request to the URL and
displays the value of the X-Request-Id
variable found in the header of the response."""

from sys import argv
import urllib.parse
import urllib.request

if __name__ == "__main__":
    url = argv[1]
    email = argv[2]

    val = {"email": email}
    # Encode the email parameter
    data = urllib.parse.urlencode(val)
    data = data.encode("utf-8")  # Data should be bytes
    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req) as respon:
        # Read the response body and decode it
        resp_body = respon.read()
        print(resp_body)
