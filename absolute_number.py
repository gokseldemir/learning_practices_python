def absolute(x):
    if x < 0:
        x = -x
        return (x)
    else:
        return(x)

x = int(input("enter a number: "))
absolute(x)
y = absolute (x)
print (y)

