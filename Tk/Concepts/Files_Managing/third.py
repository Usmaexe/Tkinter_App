import os
import second as sc
def Proba(words_occ):
	probability = {}
	for word in words_occ : 
		probability[word] = round(words_occ[word]/len(words_occ),9)
	return probability

if __name__ == "__main__" :
	words = sc.Occurence('shakespeare.txt')
	dict_proba = Proba(words)
	print(dict_proba)