import load_dictionnary as ld
from collections import Counter as ct
def subAnagram():
	print("Give me a word :")
	word = str(input())
	dictionnary = dict(ct(word))
	del dictionnary[' ']
	print(dictionnary)
	word_list = ld.load('2of4brif.txt')
	for w in word_list : 
		letters = list(w)
		exist = True
		lett = dictionnary.copy()
		for l in letters :  
			if(not(l in dictionnary)):
				exist = False
			else : 
				lett[l]-=1
		for value in lett.values() : 
			if(value<0):
				exist = False
		if(exist):
			print(w)
print(subAnagram())