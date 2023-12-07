import re
def cryptage(msg,key):
	alphabet = [chr(c) for c in range(65,91)]
	crypted = [];columns = [];size=len(msg)
	letters = [[0]*26 for i in range(26)]
	for i in range(26):
		for j in range(26):
			letters[i][j] = alphabet[(i+j)%26]
	j=0
	for i in range(size):
		if(re.match("[^A-Za-z]+",msg[i])):
			crypted.append(msg[i])
		else :
			crypted.append(letters[ord(key[j%(len(key))])-97][ord(msg[i])-97])
			j+=1
	return ''.join(crypted)

if __name__ == '__main__' : 
	message = str(input("Entrer un message a crypter(miniscule) : "))
	cle = str(input("Entrer le clé(miniscule sans espace) : "))
	print(cryptage(message,cle))
