import random
def randnom(fname):
	lines=open(fname).read().splitlines()
	print(lines)
	return random.choice(lines)
print(randnom)