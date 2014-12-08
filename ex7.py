import png, urllib2, re

#imgloc = 'http://www.pythonchallenge.com/pc/def/oxygen.png'			#this part simply copy locally the source image
#img = urllib2.urlopen(imgloc)											#pretty sure there must be a simpler way
#out = open('oxygen.png', 'w')
#out.write(img.read())
#out.close()

source = png.Reader('oxygen.png')
#print source.read()													#gives information on the size of the picture
row = list(source.read()[2])[45]										#the information is contained in the grey band in the middle of the img

#row is a list of 4-tuples. Each tuple is made of four identical numbers, at least in the grayband
#and tuples appears in blocks of seven

count = {}																#this counts the frequency of values in the tuple
for i,pixel in enumerate(row):											#just to have an idea of what kind of stuff we have
	if (i%4==0 and row[i]==row[i+1]):
		if count.has_key(pixel):
			count[pixel] += 1
		else:
			count[pixel] = 1

message=[]																#here we really extract the hidden message
for i,pixel in enumerate(row):											#by collecting only a pixel in 7 x 4
	if (i%28==0 and row[i]==row[i+1]):
		message.append(chr(row[i]))										#and taking its corresponding ascii char
hint = ''.join(message)

#the message contains a word coded as a list of numbers in square brackets

secmessage = map(int,re.search('\[(.+)\]', hint).group(1).split(', '))	

for i,digit in enumerate(secmessage):
	secmessage[i]=chr(digit)
sechint = ''.join(secmessage)

print sechint
