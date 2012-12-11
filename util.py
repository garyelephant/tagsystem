def lines(file):
	for line in file:
		yield line
	yield '\n'

def blocks(file):
	block = []
	for line in lines(file):
		if line.strip():  
			block.append(line)
		elif block:
			#print "BLOCK:"
			#print block
			yield ''.join(block).strip()
			block = []

#Question
"""
1. line.strip() ,if line == "", what will strip() return ?
"""
