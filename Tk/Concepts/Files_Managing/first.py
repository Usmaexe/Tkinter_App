import os
def lowerCase(fileName):
	file = open(fileName,'r')
	#TO DISPLAY THE CONTENT OF THE FILE ALL IN LOWER CASE
	#print(file.read().lower())
	file.close()	

def Reading(fileName):
	#TO CREATE THE LIST OF WORDS IN THE FILE WITHOUT REPETITION
	file = open(fileName,'r')
	words = []
	lines = file.readlines()
	for line in lines : 
		word = line.split()
		for each_word in word : 
			if not(each_word in words) :
				words.append(each_word)
	file.close()
	return words
if __name__ == '__main__' : 
	print(Reading('shakespeare.txt'))