def bol(x,y):
    m = x % y
    return (m)
def karekok (x,y):
    u = x ** 0.5
    return(u)

x = int(input("enter dividend: "))
y = int (input("enter  divider"))

if bol(x,y) == 0:
    print("Divisible")
else:
    print ("Not divisible")
    
