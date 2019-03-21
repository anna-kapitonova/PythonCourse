with open('rosalind_subs.txt', 'r') as file:
    dna, seq = file.readlines()
    a=len(dna)-len(seq)+1
    for i in range(a):
        b=i+len(seq)
        if dna[i:b]==seq:
            print(i+1, end='\t')
