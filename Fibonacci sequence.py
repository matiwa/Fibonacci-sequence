'''Fibonacci sequence'''

n=int(input("Enter n: "))
if n<0:
    print("The number must be greater than or equal to zero!")
else:
    #Calculating
    fib=[0,1]
    i=-1
    while i<n:
        i+=1
        if i>=2:
            fib.append(int(fib[i-1]+fib[i-2]))
        '''Write'''
        print("F("+str(i)+")="+str(fib[i]))
