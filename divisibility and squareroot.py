def div(a,b):
    m = a % b
    return (m)
def sqrt (a,b):
    u = a ** 0.5
    return(u)

x = int(input("enter divident: "))
y = int (input("enter divider: "))

if bol(a,b) == 0:
    print("divisible")
    h, j = div (a,b)
    f = sqrt(a)
    print (h, "it should definitily be 4", j, "if it is the squareroot of...", f)
else:
    print ("not divisible")
    
