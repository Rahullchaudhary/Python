# word counter
# harshit
# d={'a':1,'h':2}
def word_counter(s):
    d={}
    for i in s:
        d[i]=s.count(i)
    return d
print(word_counter('rahula'))   