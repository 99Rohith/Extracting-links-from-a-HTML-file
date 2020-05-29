#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 28 00:46:28 2020

@author: rohith
"""

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "myfile.html"
fhandle = open(url)
data = fhandle.read()

soup = BeautifulSoup(data, "html.parser")

tags = soup('a')
for tag in tags:
    # Look at the parts of a tag
    print('TAG:', tag)
    print('URL:', tag.get('href', None))
    print('Contents:', tag.contents[0])
    print('Attrs:', tag.attrs)
