#!/usr/bin/python3
"""a Python script that fetches https://alx-intranet.hbtn.io/status"""

import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as response:
        html_file = response.read()
        print("Body response:")
        print("\t- type:", type(html_file))
        print("\t- content:", html_file)
        print("\t- utf8 content:", html_file.decode("utf-8"))
