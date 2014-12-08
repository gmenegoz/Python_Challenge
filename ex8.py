import bz2, urllib2, re
url = 'http://www.pythonchallenge.com/pc/def/integrity.html'
text = urllib2.urlopen(url).read()

un = re.search('un: \'(.+)\'', text).group(1)
pw = re.search('pw: \'(.+)\'', text).group(1)

print bz2.decompress(un.decode('string_escape'))
print bz2.decompress(pw.decode('string_escape'))
