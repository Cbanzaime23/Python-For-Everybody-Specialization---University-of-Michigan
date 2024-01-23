# import json
# data = '''{
#     "name" : "Chuck",
#     "phone" : {
#         "type" : "intl",
#         "number" : "+1 734 303 4456",
#         "provider" : "Globe"
#     },
#     "email" : {
#         "hide" :  "yes"
#     }
# }'''
#
# #Dictionary
# info = json.loads(data)
# print('Name:', info["name"])
# print('Hide:', info["email"]["hide"])
# print('Provider:', info["phone"]["provider"])


# import json
# input = '''[
#     {   "id" : "039",
#         "x" : "7",
#         "name" : "Chuck1"
#     }   ,
#     {   "id" : "029",
#         "x" : "7",
#         "name" : "Chuck2"
#     }   ,
#     {   "id" : "091",
#         "x" : "2",
#         "name" : "Chuck3"
#     }   ,
#     {   "id" : "009",
#         "x" : "7",
#         "name" : "Chuck4"
#     }
# ]'''
#
# info = json.loads(input)
# print('User count:', len(info))
# for item in info:
#     print('Name', item['name'])
#     print('Id', item['id'])
#     print('Attribute', item['x'])

#Google API
# import urllib.request, urllib.parse, urllib.error
# import json
#
# serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'
#
# while True:
#     address = input('Enter location: ')
#     if len(address) < 1: break
#
#     url = serviceurl + urllib.parse.urlencode({'address': address})
#
#     print('Retrieving', url)
#     uh = urllib.request.urlopen(url)
#     data = uh.read().decode()
#     print('Retrieved', len(data), 'Characters')
#
#     try:
#         js = json.loads(data)
#     except:
#         js = None
#
#     if not js or 'status' not in js or js['status'] != 'OK':
#         print('==== Failure To Retrieve ====')
#         print(data)
#         continue
#
#     print(json.dumps(js, indent = 4))
#
#     lat = js["results"][0]["geometry"]["location"]["lat"]
#     lng = js["results"][0]["geometry"]["location"]["lng"]
#     print('lat', lat, 'lng', lng)
#     location = js['results'][0]['formatted_address']
#     print(location)


# import urllib.request, urllib.parse, urllib.error
# import xml.etree.ElementTree as ET
# import ssl
#
# api_key = False
# # If you have a Google Places API key, enter it here
# # api_key = 'AIzaSy___IDByT70'
# # https://developers.google.com/maps/documentation/geocoding/intro
#
# if api_key is False:
#     api_key = 42
#     serviceurl = 'http://py4e-data.dr-chuck.net/xml?'
# else :
#     serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'
#
# # Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE
#
# while True:
#     address = input('Enter location: ')
#     if len(address) < 1: break
#
#     parms = dict()
#     parms['address'] = address
#     if api_key is not False: parms['key'] = api_key
#     url = serviceurl + urllib.parse.urlencode(parms)
#     print('Retrieving', url)
#     uh = urllib.request.urlopen(url, context=ctx)
#
#     data = uh.read()
#     print('Retrieved', len(data), 'characters')
#     print(data.decode())
#     tree = ET.fromstring(data)
#
#     results = tree.findall('result')
#     lat = results[0].find('geometry').find('location').find('lat').text
#     lng = results[0].find('geometry').find('location').find('lng').text
#     location = results[0].find('formatted_address').text
#
#     print('lat', lat, 'lng', lng)
#     print(location)



# data = '''
# [
#   { "id" : "001",
#     "x" : "2",
#     "name" : "Chuck"
#   } ,
#   { "id" : "009",
#     "x" : "7",
#     "name" : "Brent"
#   } ,
#   { "id" : "023",
#     "x" : "9",
#     "name" : "Ian"
#   }
# ]'''
#
# info = json.loads(data)
# print('User count:', len(info))
#
# for item in info:
#     print('Name', item['name'])
#     print('Id', item['id'])
#     print('Attribute', item['x'])

# import json
# import urllib.request, urllib.parse, urllib.error
#
# count = 0
# sum = 0
#
# url = input('Enter Location: ')
# print("Retrieving " + url)
#
# data = urllib.request.urlopen(url)
# info = json.loads(data.read())
# # print(info)
# for item in info["comments"]:
# 	count += 1
# 	sum += item["count"]
#
# print('Count: ', count)
# print('Sum: ', sum)



import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    #print(json.dumps(js, indent=4))

    #lat = js['results'][0]['geometry']['location']['lat']
    #lng = js['results'][0]['geometry']['location']['lng']
    #print('lat', lat, 'lng', lng)
    #location = js['results'][0]['formatted_address']
    #print(location)
    PlaceID = js['results'][0]['place_id']
    print("Place id "PlaceID)
