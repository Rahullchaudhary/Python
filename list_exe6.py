def count_list(l):
    count=0
    b=type(l)
    for i in l:
        if(type(i)==list):
            count =count+1
    return count
num=[1,2,3,[3,5,4],8,[0,4,7,6]]
print(count_list(num))