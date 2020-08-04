# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
j=list()
contador=0
tags = soup('span')
for tag in tags:

    x=tag.decode()
    if re.findall('\d',x):
        j=re.split('\W',x)
        contador=contador+int(j[6])
print(contador)
        
    
    
