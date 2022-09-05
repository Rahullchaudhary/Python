f_name="Rahul"
l_name=" Chaudhary"
full_name=f_name+""+l_name
#print(full_name)
#print(f_name+3)#it gives type error
#print(f_name+str(3))#no error
#print(f_name*3)


#User input
#name=input("type your name")
#print(name)
# num1=int(input("Enter first number\n"))
# num2=int(input("Enter second number\n"))
# total=num1+num2
# print(total)
# name,age="Rahul","20"
# print("hello "+ name+ " your age is "+age)
name,age=input("Enter your name and age").split()
print(name,age)

