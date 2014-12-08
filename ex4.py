import urllib2
baseurl='http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
codeurl='12345'
i = 0
while i < 300:
	chainurl=baseurl+codeurl
	webpage=urllib2.urlopen(chainurl)
	codeurl=webpage.read().split()[-1] #the last word is the next address
	i += 1
	try:
		int(codeurl)
	except ValueError: #if the last word of the code is not a number then print it
		print codeurl
