import urllib2
from PIL import Image
from itertools import product

imgloc = 'http://www.pythonchallenge.com/pc/return/cave.jpg'
usr = 'huge'
pwd = 'file'

passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
passman.add_password(None, imgloc, usr, pwd)
authhandler = urllib2.HTTPBasicAuthHandler(passman)
opener = urllib2.build_opener(authhandler)
urllib2.install_opener(opener)

#img = urllib2.urlopen(imgloc)
#out = open('cave.jpg', 'w')
#out.write(img.read())
#out.close()

im = Image.open('cave.jpg', 'r')
iml = im.load()


one = Image.new('RGB',(320,240),'red')
for x,y in product(range(0,320),range(0,240)):
	one.load()[x,y] = tuple([10*i for i in iml[2*x,2*y]])
	one.show()
