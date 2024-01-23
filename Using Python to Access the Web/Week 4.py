# import urllib.request, urllib.parse, urllib.error
#
# fhand = urllib.request.urlopen('http://data.pr4e.org/intro-short.txt')
# for line in fhand:
#     print(line.decode().strip())


# import urllib.request, urllib.parse, urllib.error
#
# fhand = urllib.request.urlopen('http://data.pr4e.org/intro-short.txt')
#
# counts = dict()
# for line in fhand:
#     words = line.decode().split()
#     for word  in words:
#         counts[word] = counts.get(word, 0) + 1
# print(counts)


#Reading Webpages
# import urllib.request, urllib.parse, urllib.error
#
# fhand = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
# for line in fhand:
#     print(line.decode().strip())

# import urllib.request, urllib.parse, urllib.error
# from bs4 import BeautifulSoup
# import ssl
# import re
#
# #Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE
#
# url = input('Enter - ')
# html = urllib.request.urlopen(url).read()
# soup = BeautifulSoup(html, 'html.parser')
#
# #retrieve all of the anchor tags
# # Retrieve all of the anchor tags
# tags = soup('span')
# numlist = list()
# count = 0
# for tag in tags:
#     tag = str(tag)
#     nums= re.findall('[0-9]+', tag)
#     count = count + 1
#     nums = int(''.join(nums))
#     #print(nums)
#     numlist.append(nums)
# print('Count ', count)
# print('Sum ', sum(numlist))

# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

# import urllib.request, urllib.parse, urllib.error
# from bs4 import BeautifulSoup
# import ssl
#
# # Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE
#
# EnterUrl = input('Enter URL:')
# EnterCount = input('Enter count:')
# EnterPosition = input('Enter position:')
# count = 0
#
# html = urllib.request.urlopen(EnterUrl, context=ctx).read()
# soup = BeautifulSoup(html, 'html.parser')
#
# # Retrieve all of the anchor tags
# tags = soup('a')
# for tag in tags:
#     count = count + 1
#     if count == int(EnterPosition):
#         EnterUrl = (tag.get('href', None))
#         html = urllib.request.urlopen(EnterUrl, context=ctx).read()
#         soup = BeautifulSoup(html, 'html.parser')
#         print(tag.get('href', None))

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Set an input function for the url address and parse it through BeautifulSoup
url = input('Enter URL : ')
html = urllib.request.urlopen(url, context = ctx).read()
soup = BeautifulSoup(html, 'html.parser')

#Set up an input functions for the repeat
count = int(input('Enter count : '))

#Set up an input function for the position
position = int(input('Enter position : '))

#Initialize currcount to 0
currcount = 0

print("Retrieving: ", url)
#Repeat the loop for the required amount of repeats
while currcount < count :
    # Retrieve the url for the required position and print it
    tags = soup('a')
    for tag in tags:
    	tag = tags[position - 1].get('href', None)
    print("Retrieving : " + tag)

    #Parse the new link
    html = urllib.request.urlopen(tag, context = ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    #Increment currcount
    currcount = currcount + 1
