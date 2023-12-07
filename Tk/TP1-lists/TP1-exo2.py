def crypto(s,key):
    c=[]
    line = int(len(s)/key)
    for i in range(key):
        for j in range(line+1) :
            if(key*j+i<len(s)):
                print(s[key*j+i],key*j+i)
                c.append(s[key*j+i])
    c.append("|")
    return "".join(c)
print(crypto("Common sense is not so common.",8))

