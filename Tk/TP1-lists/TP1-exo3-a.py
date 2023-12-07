import load_dictionnary as ld
def Anagram():
	print("Give me a word :")
	word = str(input())
	word_list = ld.load('2of4brif.txt')
	an = []
	for i in range(1,len(word)+1) : 
		an.append(word[-i])
	an = "".join(an)
	for w in word_list : 
		if(w==an):
			print(w)
	
print(Anagram())