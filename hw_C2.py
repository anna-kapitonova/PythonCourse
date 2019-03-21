a=input()
b=[int(symbol) for symbol in a]
summ=0
pr=1
for i in range(len(b)):
    summ+=b[i]
    pr=pr*b[i]
print('Сумма цифр:', summ)
print('Произведение цифр:', pr)
