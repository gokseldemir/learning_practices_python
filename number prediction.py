import random
sayi = random.randint(1,100)
x=0
print(sayi)
while True:
    x = x + 1
    i=int(input('predict a number between 1 and 100!'))
    if i == sayi:
        print('Well done! You predicted %s.....%s ' % (i, x))
        break
    elif i < sayi:
        print('It is larger than your prediction')
    elif i > sayi:
        print('It is smaller than your prediction')
