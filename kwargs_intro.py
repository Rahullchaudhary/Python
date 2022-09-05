def func(**kwargs):
    # print(kwargs)
    # print(type(kwargs))
    for i,j in kwargs.items():
        print(f"{i}:{j}")
# func(first_name='Rahul',last_name='chaudhary') 
d={'name':'Rahul','age':'20'}
func(**d)   