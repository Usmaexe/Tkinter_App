##USING ONE OF THE MY PRE-BUILT FUNCTIONS TO RETRIEVE WORDS FROM A FILE
from first import Reading as rd
from second import Occurence as oc
from third import Proba
from forth import *

def Correction(word,vocabulary,n):

	words = []
	if word in vocabulary :
		words.append(word)
		n-=1

	Swaping = Swap(word)
	Swaping.remove(word)
	words = Delete(word) + Swaping + Replace(word) + Add(word)

	for w in words :
		if not(w in vocabulary) : 
			words.remove(w)
	

	#On which file Sould we check the occurences
	file_words = oc('shakespeare.txt')
	dict_proba = Proba(file_words)

	#A list should be sorted based on the probability
	print(words)
	for w in words : 
		if w in dict_proba :
			print(dict_proba[w],w)
	
if __name__ == "__main__" : 
	vocabulary = rd('2of4brif.txt')
	Correction("dys",vocabulary,2)