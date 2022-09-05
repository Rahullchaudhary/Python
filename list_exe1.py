def squre_list(l):
    squre=[]
    for i in l:
        # squre.append(i*i)
        squre.append(i**2)
    return squre    
# number= [1,2,3,4,5,6,7]
number=list(range(1,11))
print(squre_list(number))
      