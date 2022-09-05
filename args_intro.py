# def all_toatal(*args):
#     total=0
#     print(type(args))
#     for i in args:
#         total +=i
#     return total
# print(all_toatal(1,2,3,4))   


# ==================

# def multiple_num(num,*args):
def multiple_num(num,*args): 
    multiply=1
    print(num)
    print(args)
    for i in args:
        multiply *=i
    return multiply
print(multiple_num(2,3,4))        