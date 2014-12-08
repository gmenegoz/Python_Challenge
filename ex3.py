import string, re, urllib2

text = urllib2.urlopen('http://www.pythonchallenge.com/pc/def/equality.html').read()
mess = re.search(r'<!--(.+)-->', text, re.DOTALL).group(0).replace('\n','')
patt_re = re.compile('[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]') 
patt = patt_re.findall(mess)
print ''.join(patt)


#for i,letter in enumerate(mess):
#	if letter in string.ascii_lowercase:
#		shoulder=mess[i-3:i]+mess[i+1:i+4]
#		if shoulder.isupper() and mess[i-4] in string.ascii_lowercase and mess[i+4] in string.ascii_lowercase:
#			print mess[i],
			


				

