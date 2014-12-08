from string import maketrans
import string
secret = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. "


oldtable = string.ascii_lowercase
newtable = oldtable[2:]+oldtable[:2]
	
	
table=maketrans(oldtable,newtable)

solution = secret.translate(table)

print solution
print "map".translate(table)
