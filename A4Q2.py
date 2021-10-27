n=int(input("n = "))
m=int(input("m = "))
for i in range(1,m+1):	
    for j in range(1,n+1):
        if (j % 2 == 0):
            if (i % 2 == 0):
                print("#",end='')
            else:
                print("*",end='')
        else:
            if (i % 2 == 0):
                print("*",end='')
            else:
                print("#",end='')
        if (j == n):
            print(end='\n')