fruits1=['apple','banana','kiwi']
fruits=['apple','kiwi','banana']

fruits2=['mango','papaya','grapes']
# print(fruits1==fruits)
# print(fruits1 is fruits)
# number=list(range(1,11))
number=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(number)
# print(number.pop())
# print(number.index(1,10,14))
def negative_list(l):
    negative=[]
    for i in l:
        negative.append(-i)
    return negative
print(negative_list(number))        