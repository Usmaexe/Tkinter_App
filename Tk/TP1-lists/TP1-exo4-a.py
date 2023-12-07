from load_dictionary import load

def palindrom() : 
	words = load("2of4brif.txt")
	for w in words : 
		pal = True
		for i in range(len(w)) : 
			if(w[i]!=w[-i-1]):
				pal = False
		if(pal):
			print(w)
palindrom()
					
