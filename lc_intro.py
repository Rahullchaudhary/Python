# squares=[]
# for i in range(1,11):
#     squares.append(i**2)
# print(squares)  
# squares1=[i**2 for i in range(1,11)]  
# print(squares)

# negative=[]
# for i in range(1,11):
#     negative.append(-i)
# print(negative)

# negative1=[-i for i in range(1,11)]
# print(negative1)    
names=['rahul','salman','jay']
new_list=[]
for name in names:
    new_list.append(name[0])
print(new_list)    
name1=[name[0] for name in names]
print(new_list)