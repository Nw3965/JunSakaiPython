for i in range (1,1000000000000000000000000):
    print('What number is divisible by seven')
    x= input()
    while int(x):
        if int(x)%7 == 0:
            print("Yes")
            break
        else:
            print("no")
            break
            #7で割り切れるならYES、そうでないならNO
            #参考
            #https://itsakura.com/python-while
            
