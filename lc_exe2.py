def num_To_string(l):
    return [str(i) for i in l if (type(i)==int or type(i)==float)]

print(num_To_string([True,False,[1,2,3],1,1.0,3]))    