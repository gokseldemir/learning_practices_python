expression = input("Mantıksal iŞlemi girin : and veya or gibi ")
print(" p      q      %s"  % expression)
length = len( " p      q      %s"  % expression)
print(length * "=")
if expression == 'and':
    for p in True, False:
        for q in True, False:
            son = p and q
            print ("%-7s %-7s %-7s" % (p, q, son))
elif expression == 'or':
    for p in True, False:
        for q in True, False:
            son = p or q
            print ("%-7s %-7s %-7s" % (p, q, son))
else:
    print('Lütfen tekrar giriş yapın!')
    
