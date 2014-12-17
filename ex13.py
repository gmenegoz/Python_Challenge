import xmlrpclib

server = xmlrpclib.ServerProxy('http://www.pythonchallenge.com/pc/phonebook.php')

#print server.ping()
print server.system.listMethods()
#print server.phone('Bert')
