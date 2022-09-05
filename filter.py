def is_even(a):
    return a%2==0
numbers=[3,2,4,6,5,8,10]
evens=tuple(filter(is_even,numbers)) 
print(evens)  
evens=tuple(filter(lambda a:a%2==0,numbers))
print(evens) 
for i in evens:
    print(i) 