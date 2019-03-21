a=input()
b=[int(symbol) for symbol in a.split(',')]
c=[]
for i in range(len(b)-1):
        if b[i+1]>=b[i]:
           c.append(b[i+1])
print(c)
