import re
def decrypt(msg,key) : 
	alphabet = [chr(c) for c in range(65,91)]
	letters = [[0]*26 for i in range(26)]
	size = len(msg);decrypt = '';
	for i in range(26):
		for j in range(26):
			letters[i][j] = alphabet[(i+j)%26]
	j=0
	for letter in msg : 	
		if(re.match("[^A-Za-z]+",letter)):
			decrypt+=letter
		else : 
			for col in range(26) : 
				if(letters[ord(key[j%len(key)])-65][col]==letter.upper()):
					decrypt+=chr(col+65)
			j+=1
	return decrypt
message = str(input("Entrer un chiffrage a décrypter : "))
cle = str(input("Entrer le clé(sans espace) : "))
print(decrypt(message,cle))