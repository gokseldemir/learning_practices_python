def multiplicationtable(satir, sütun):
    i = 1
    while i <= satir:
        j = 1
        while j <= i:
            print(j*i, "\t", end="")
            j = j+1
        print("\t")
        i = i + 1
        print()
multiplicationtable(7 , 7)
                
