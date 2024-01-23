# import socket
#
# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect(('data.pr4e.org', 80))
# cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
# mysock.send(cmd)
#
# while True:
#     data = mysock.recv(512)
#     if (len(data < 1)):
#         break
#     print(data.decode())
# mysock.close()


#Our First Class and Object

# class PartyAnimal:
#     x = 0
#
#     def party(self):
#         self.x = self.x + 1
#         print("So far", self.x)
#
# an = PartyAnimal()
#
# an.party()
# an.party()
# an.party()
# an.party()
# an.party()
# an.party()
#
# PartyAnimal.party(an)
#
#
# print("Type", type(an))
# print("Dir", dir(an))


# class PartyAnimal:
#     x = 0
#
#     def __init__(self):
#         print('I am constructed')
#
#     def party(self):
#         self.x = self.x + 1
#         print('So far', self.x)
#
#     def __del__(self):
#         print('I am destructed', self.x)
#
# an = PartyAnimal()
# an.party()
# an.party()
# an = 42
# print('an contains', an)

class PartyAnimal:
    x = 0
    name = ""

    def __init__(self, z):
        self.name = z
        print(self.name, 'constructed')

    def party(self):
        self.x = self.x + 1
        print(self.name, 'party count', self.x)

# s = PartyAnimal("Sally")
# s.party()
#
# j = PartyAnimal("Jim")
# j.party()
# s.party()


#This is just an Inheretance of PartyAnimal
#An EXTENSION of Party Animal
class FootballFan(PartyAnimal):
    points = 0
    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print(self.name, "points", self.points)


s = PartyAnimal("Sally")
s.party()


j = FootballFan("Jim")
j.party() #Capability from PartyAnimal
j.touchdown() #Capability form  FootballFan
