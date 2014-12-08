import re

seed = '1'
block_re = re.compile(r'((\d)\2*)')

def next_seed(seed):
	new_seed = ''
	block = block_re.findall(seed)
	for i,tup in enumerate(block):
		block[i] = tup[0]
	for el in block:
		new_seed += str(len(el))+ el[0]
	return new_seed

i=1
while i<35:
	print i, len(next_seed(seed))
	seed = next_seed(seed)
	i +=1
