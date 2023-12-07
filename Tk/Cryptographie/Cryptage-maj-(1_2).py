T=[[0]*26 for i in range(26)]
L=[]
for i in range(26):
	L.append(chr(65+i))
for i in range(26):
	for j in range(26):
		T[i][j]=L[(i+j)%26]
txt=input('Donnez un texte à decrypter en majuscule:')
cle=input('Donnez la clé en majuscule:')
cle_crypte=''
j=0
for i in range(len(txt)):
	if txt[i] not in L:
        	cle_crypte=cle_crypte+' '
	elif txt[i] != ' ' :
		cle_crypte=cle_crypte+cle[j%(len(cle))]
	j=j+1
cryptage=''
for i in range(len(txt)):
	if txt[i] in L:
		a=L.index(txt[i])
		b=L.index(cle_crypte[i])
		cryptage=cryptage+T[a][b]
	else:
		cryptage=cryptage+txt[i]
print('Le texte crypte est le suivant:',cryptage)

