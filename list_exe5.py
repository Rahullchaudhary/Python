# def same_element(l,m):
#     elements=[]
#     for i in l:
#         for j in m:
#             if(i==j):
#                 elements.append(i)
#     return elements
# nums=list(range(1,6))
# num=list(range(3,8))
# print(same_element(nums,num))    
def same_element(l,m):
    elements=[]
    for i in l:
        if(i in m):
            elements.append(i)
    return elements
nums=list(range(1,6))
num=list(range(3,8))
print(same_element(nums,num))                            