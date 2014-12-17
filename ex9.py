import urllib2, re
from PIL import Image

theurl = 'http://www.pythonchallenge.com/pc/return/good.html'
usr = 'huge'
pwd = 'file'

passman = urllib2.HTTPPasswordMgrWithDefaultRealm()						# this block enables authentication for urlopen method
passman.add_password(None, theurl, usr, pwd)
authhandler = urllib2.HTTPBasicAuthHandler(passman)
opener = urllib2.build_opener(authhandler)								# creates an opener objects that manages authentication at any use of urllib2
urllib2.install_opener(opener)

text = urllib2.urlopen(theurl).read()
first_re = re.compile('first:\n([\d,\n]*)\n{2}')
second_re = re.compile('second:\n([\d,\n]*)\n{2}')
first = map(int,first_re.findall(text)[0].split(','))
second = map(int,second_re.findall(text)[0].split(','))


i = Image.new("RGB", (512,512), "white")
p=i.load()

for x in range(len(first)/2):
    p[first[x*2],first[x*2+1]] = (255, 0, 0)
for x in range(len(second)/2):
    p[second[x*2],second[x*2+1]] = (0, 0, 255)
i.show()
