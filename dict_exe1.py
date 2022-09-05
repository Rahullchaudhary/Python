def cube_finder(a):
    d={}
    for i in range(1,a+1):
        d[i]=i**2
    return d
print(cube_finder(3))        