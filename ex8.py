import bz2, urllib2, re
url = 'http://www.pythonchallenge.com/pc/def/integrity.html'
text = urllib2.urlopen(url).read()

un = re.search('un: \'(.+)\'', text).group(1)							# selects user and password from the html source
pw = re.search('pw: \'(.+)\'', text).group(1)							# but they are bz2 encoded (write better)

print bz2.decompress(un.decode('string_escape'))
print bz2.decompress(pw.decode('string_escape'))
