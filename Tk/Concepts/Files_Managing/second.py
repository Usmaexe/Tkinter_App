import os
def Occurence(fileName):
	file = open(fileName,'r')
	words = []
	lines = file.readlines()
	for line in lines : 
		word = line.split()
		for each_word in word : 
			if not(each_word in words) :
				words.append(each_word)
	dictionnary = {word : 0 for word in words}
	file.close()

	file = open(fileName,'r')
	for line in lines : 
		word = line.split()
		words.extend(word)
	for word in words:
		if(word in dictionnary):
			dictionnary[word]+=1	
	return dictionnary
	file.close()
if __name__ == '__main__':
	words_occ = {}
	words_occ = Occurence('shakespeare.txt')
	print(words_occ)