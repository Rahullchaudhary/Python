def fib(num):
    while(num>0):
        n1=0
        n2=1
        print(n1,n2,end=",")
        n3=n1+n2
        n1=n2
        n2=n3
        print(n3,end=",")
        num=num-1 
fib(7)     