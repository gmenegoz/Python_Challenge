import urllib2, pickle, sys
url = 'http://www.pythonchallenge.com/pc/def/banner.p'
tup = pickle.load(urllib2.urlopen(url)) #decodes the original file, which contains a tuple of lists
for line in tup: 						#iterates on elements of the tuple, corresponding to different lines of the output
	for el in line: 					#iterates in element of the line, corresponding to a tuple like ('#', 10)
		sys.stdout.write(el[0]*el[1]),	#allows to write without \n and spaces 
	sys.stdout.write('\n'),
