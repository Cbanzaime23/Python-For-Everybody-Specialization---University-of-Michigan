#Web Services

# import xml.etree.ElementTree as ET
#
# data = '''<person>
#     <name>Chuck</name>
#     <phone type = "intl">+1 734 303 4456</phone>
#     <email hide = "yes"/>
# </person>'''
#
# tree = ET.fromstring(data)
# print('Name:', tree.find('name').text)
# print('Attr:', tree.find('email').get('hide'))
# print('Phone:', tree.find('phone').text)




# import xml.etree.ElementTree as ET
# input = '''
# <commentinfo>
#     <note>This file contains the actual data for your assignment - good luck!</note>
#     <comments>
#         <comment>
#             <name>Asfhan</name>
#             <count>98</count>
#         </comment>
#         <comment>
#             <name>Hillary</name>
#             <count>97</count>
#         </comment>
#         <comment>
#             <name>Leea</name>
#             <count>95</count>
#         </comment>
# </commentinfo>'''
#
# stuff = ET.fromstring(input)
# lst = stuff.findall('comment')
# print(lst)
# print('User count:', len(lst))

# for item in lst:
#     print('Name', item.find('name').text)
#     print('Id', item.find('id').text)
#     print('Attribute',item.get("x"))
#
# lst = stuff.findall('users/user/id')
# print(lst)

#Sample Data: http://py4e-data.dr-chuck.net/comments_1071443.xml

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

#Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

count = 0
Total = list()

address = input('Enter location: ')

print('Retrieving ' + address)
data = urllib.request.urlopen(address, context = ctx).read()

tree  = ET.fromstring(data)
lst = tree.findall('.//count')

for item in lst:
    #count += 1
    item = int(item.text)
    Total.append(item)
#
print('Count: ', len(Total))
print('Sum: ', sum(Total))
