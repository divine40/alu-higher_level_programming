#!/usr/bin/python3
"""__summary__
- Write a Python script that fetches https://alu-intranet.hbtn.io/status
- using the urllib package.
"""
import urllib.request


if __name__ == '__main__':
     with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        content = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode("utf-8")))
	""" the method i used is easy way for string manipulation
            to use a method that make use of the concept
            print out html.decode('utf-8') with string formatting
        """
	temp = str(content)
	print("\t- utf8 content: {}".format(temp[2:-1]))
