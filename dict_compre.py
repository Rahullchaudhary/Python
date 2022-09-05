# square={num:num**2 for num in range(1,11)}
# print(square)
square={f"Square of {num} is":num**2 for num in range(1,11)}
for k,v in square.items():
    print(f"{k}:{v}")

str1="Rahula"
word_count={char:str1.count(char) for char in str1}  
print(word_count)  