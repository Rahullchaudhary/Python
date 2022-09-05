# def reverse_list(l):
#      l.reverse()
#      return l
# def reverse_list(l):
#      return l[::-1]
def  reverse_list(l):
    reverse=[]
    for i in range(len(l)):
        reverse.append(l.pop())
    return reverse
number=list(range(1,11))
print(reverse_list(number))        