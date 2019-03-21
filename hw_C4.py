a, b, c=(float(i) for i in input().split(','))
D=b**2-4*a*c
if D>0:
    if a!=0:
        x1=(-b+D**0.5)/(2*a)
        x2=(-b-D**0.5)/(2*a)
        print(x1, x2)
    else:
        x=-c/b
        print(x)
elif D==0:
    x=-b/(2*a)
    print(x)
else:
    print('Действительных корней нет')
