def filter_odd_even(l):
    odd_nums=[]
    even_nums=[]
    for i in l:
        if(i%2==0):
            even_nums.append(i)
        else:
            odd_nums.append(i)
    output=[odd_nums,even_nums] 
    return output
nums=list(range(1,11))     
print(filter_odd_even(nums))         