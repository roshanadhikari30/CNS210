def fibonacci1(num):
    F0 = 0
    F1 = 1
    counter = -1
    while counter < num:
        print(F0)
        with open("C:/pY/pythonCode/fibo.txt","a+") as out:
            out.write(str(F0)+'\n')
        F2 = F0 + F1
        F0 = F1
        F1 = F2
        counter += 1 
fibonacci1(5)
#with open("fibo.txt","a+") as out:
    #out.write(str(fibonacci1(5))+'\n'
