import zipfile		# the zipfile library contains method to manipulate zip files

root = '/home/menegoz/Computer/Python/Challenge/channel/'
old = '90052'
ext = '.txt' 
 
i = 0
while (i < 910): 	# there are 909 files (must find a way to count the number of files)
	txtfile = root + old + ext
	try:
		new = open(txtfile, 'r').read() 		# tries to open the next file in the series and take the last word,
		old = new.split()[-1]					# which is supposed to be a number
	except IOError: 
		print new  								#if it's not, then prints what it found
	i +=1
	
#this only gives you the hint of reading the comments of the different files in the archive

myzip = zipfile.ZipFile('/home/menegoz/Computer/Python/Challenge/channel.zip', 'r') # this loads the zipfile
print myzip.open('90052.txt').read()  												# this reads the content of single file

#the myzip.filelist list is a bad looking object, made by pointers, not filenames

mydict = [(m.filename.split('.')[0], m.comment) for m in myzip.filelist]  # creates a dictionary of (filename, comment)
print mydict									                          # totally useless for the result, but it's just to learn how it works						

old = '90052'

while True:
	try:
		print myzip.getinfo(old+ext).comment,            # the getinfo method extracts pieces of info (e.g. the comment) from the specified file
		old=myzip.open(old+ext).read().split()[-1]       # the usual iteration to follow the chain of files
	except IOError:
		print old                                        # 
	except KeyError:
		break                                            # stops the iteration if no more files are found
