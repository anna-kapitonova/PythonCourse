s=input()
sp=s.split()
word=sp[0]
for i in range(len(sp)-1):
    if len(sp[i+1])<len(word):
        word=sp[i+1]
print(word)
