def function1(l,**kwargs):
    if kwargs.get('reverse_str')==True:
        return [i[::-1].title() for i in l]
    else:
        return [name.title() for name in l]    
name=['rahul','salman']
print(function1(name,reverse_str=True))      