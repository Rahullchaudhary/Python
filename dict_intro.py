# creating dict
# user={'name':'Rahul','age':'21'}
user=dict(name='Rahul',age=21)
# print(user)
# print(type(user))
# access data from dict
# using key 
# print(user['name'])
user_info={
    'name':'Rahul',
    'age':21,
    'fav_movie':['hollywood','south'],
}
# print(user_info['fav_movie'])
# how to add data in empty dict
user1={}
user1['name']='mohit'
# print(user1)

# in keyword in dict
# if 'names' in user_info:
#     print('present')
# else:
#     print('not present:')    


# for values
# if 21 in user_info.values():
#     print('present')
# else:
#     print('not present:')    


# loops
# for i in user_info.values():
#     print(i)

# values method
# user_info_values=user_info.values()
# print(user_info_values)
# print(type(user_info_values))


# keys method
# user_info_values=user_info.keys()
# print(user_info_values)
# print(type(user_info_values))

# 
# for i in user_info:
#     print(user_info[i])
# 

# items method
user_items=user_info.items()
# print(user_items)
# print(type(user_items))

# for key,value in user_info.items():
#     print(f"key is {key} and value is {value} ")

# how to add data
user_info['fav_song']=['song1','song2']
# print(user_info)


# pop method
# pop_item=user_info.pop('fav_song')
# print(pop_item)
# print(user_info)


# === popitem method
# pooped_item=user_info.popitem()
# print(user_info)
# print(type(pooped_item))

# ==== update method
more_info={'state':'haryana','hobbies':['coading','reading','cricket']}
user_info.update(more_info)
# print(user_info)




#  ==== fromkeys ====
# d=dict.fromkeys(['name','age','height'],'unknown')
# d=dict.fromkeys('abc','unknown')
d=dict.fromkeys(range(1,11),'unknown')
print(d)