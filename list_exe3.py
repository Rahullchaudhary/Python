def string_revere(l):
    reverse_string=[]
    for i in l:
        reverse_string.append(i[::-1])
    return reverse_string    
string=['abc','tuv','xyz']
print(string_revere(string))    