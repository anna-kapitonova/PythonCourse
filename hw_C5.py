m, f=(int(i) for i in input().split())
n=[1, 1+f]
c=1+f
for i in range(m-3):
    c+=f*n[i]
    n.append(c)
print(c)
