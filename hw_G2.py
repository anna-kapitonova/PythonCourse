def generator(start, end):
    current=start
    i=2
    while current < end:
        while i<current:
            if current%i==0:
                current+=1
            else:
                i+=1
                if i==current:
                    yield current
                    current+=1
                    i=2
                if current==end:
                    break
