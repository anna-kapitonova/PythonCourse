with open('rosalind_hamm.txt', 'r') as file:
    a, b = file.readlines()
    count=0
    for i in range(len(a)):
            if a[i]!=b[i]:
                count+=1      
    print(count)
