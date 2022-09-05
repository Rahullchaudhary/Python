names=['abe','Rahul','Chaudhary']
# pos=0
# for i in names:
#     print(f'{pos}---->{i}')
#     pos +=1
# for pos,name in enumerate(names):
#     print(f'{pos}---->{name}')

def find_pos(l,target):
    for pos,i in enumerate(l):
        if i==target:
            return pos
    return -1
print(find_pos(names,'Rahul'))        