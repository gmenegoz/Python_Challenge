import zipfile

root = '/home/menegoz/Computer/Python/Challenge/channel/'
old = '90052'
ext = '.txt' 
 
i = 0
while (i < 910): #there are 909 files
	oldname = root + old + ext
	try:
		new = open(oldname, 'r').read() 		#tries to open the next file in the series and take the last word,
		old = new.split()[-1]					#which is supposed to be a number
	except IOError: 
		print new  								#if it's not, then prints what it found
	i +=1
	
#this only gives you the hint of reading the comments of the different files in the archive

myzip = zipfile.ZipFile('/home/menegoz/Computer/Python/Challenge/channel.zip', 'r') #this loads the zipfile
print myzip.open('90052.txt').read()  												#this reads the content of single file

#the myzip.filelist list is a bad looking object, made by pointers, not filenames

mydict = [(m.filename.split('.')[0], m.comment) for m in myzip.filelist]  
print mydict

old = '90052'

while True:
	try:
		print myzip.getinfo(old+ext).comment,
		old=myzip.open(old+ext).read().split()[-1]
	except IOError:
		print old
	except KeyError:
		break
