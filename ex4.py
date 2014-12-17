import urllib2
baseurl='http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
codeurl='12345'
i = 0
while i < 300:
	chainurl=baseurl+codeurl
	webpage=urllib2.urlopen(chainurl)	#this method opens a webpage
	codeurl=webpage.read().split()[-1] #the last word (addressed as '-1') is the next codeurl
	i += 1
	try:
		int(codeurl)	#tries to turn codeurl into an integer, this should work if it's a number
	except ValueError: #if the last word of the code is not a number then print it
		print codeurl
