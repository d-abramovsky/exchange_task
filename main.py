def change(money, x, y, z):
    counter = 0
    while(money>=0):
        n_money = money
        while(n_money>=0):
            if(n_money%z==0):
                counter+=1
            n_money -= y
        money -= x
    return counter

def vct(n):
    if(n == 0):
        return 1
    elif(n<2):
        return 0
    elif(2<=n<3):
        return vct(n-2)
    elif(3<=n<5):
        return vct(n-2) + vct(n-3)
    elif(5<=n<8):
        return vct(n-2) + vct(n-3) - vct(n-5)
    elif (8<=n<10):
        return vct(n-2) + vct(n-3) - vct(n-5) + vct(n-8)
    elif (10<=n<11):
        return vct(n-2) + vct(n-3) - vct(n-5) + vct(n-8) - vct(n-10)
    elif(11<=n<13):
        return vct(n-2) + vct(n-3) - vct(n-5) + vct(n-8) - vct(n-10) - vct(n-11)
    else:
        return vct(n-2) + vct(n-3) - vct(n-5) + vct(n-8) - vct(n-10) - vct(n-11) + vct(n-13)

print(change(27, 8, 3, 2))
print(vct(27))
