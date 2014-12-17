import png, urllib2, re

#imgloc = 'http://www.pythonchallenge.com/pc/def/oxygen.png'			# this part simply copy locally the source image
#img = urllib2.urlopen(imgloc).read()									# pretty sure there must be a simpler way
#out = open('oxygen.png', 'w')
#out.write(img)
#out.close()

source = png.Reader('oxygen.png')
#print source.read()													# gives information on the size of the picture the [2] part is the actual content
row = list(source.read()[2])[45]										# the information is contained in the grey band in the middle of the img
																		# but everything must be listed to be read
#row is a list of 4-tuples. Each tuple is made of four identical numbers, at least in the grayband (there is stuff at the end of the row to be discarded)
#and tuples appears in blocks of seven

count = {}																# this counts the frequency of values in the tuple
for i, pixel in enumerate(row):											# just to have an idea of what kind of stuff we have
	if (i % 4 == 0 and row[i] == row[i + 1]):							# select the first elem of a tuple if it is identical to the second one
		if count.has_key(pixel):										# if the element was already seen we update the count
			count[pixel] += 1
		else:
			count[pixel] = 1											# otherwise we add it to the dictionary

message = []															# here we really extract the hidden message
for i, pixel in enumerate(row):											# by collecting only a pixel every 7 x 4
	if (i % 28 == 0 and row[i] == row[i + 1]):
		message.append(chr(row[i]))										# and taking its corresponding ascii char
hint = ''.join(message)													# all the chars are joined to for a message		

#the message contains a word coded as a list of numbers in square brackets

secmessage = map(int,re.search('\[(.+)\]', hint).group(1).split(', '))	# the group 1 of the regexp selects stuff inside the [], elements are splitted 
																		# and batch converted to integers
for i, digit in enumerate(secmessage):
	secmessage[i] = chr(digit)
sechint = ''.join(secmessage)

print sechint
