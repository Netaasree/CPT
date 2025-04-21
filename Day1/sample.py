"""
#write a porgram to swap two numbers using circumflex
a=1 #0001
b=2 #0010
    
a=a^b #0011-3
b=a^b
a=a^b
print(a)
print(b)

#swap 2 numbers using conditional swap by logical AND/OR
a=1
b=2
temp=a
a=(a|b)&b 
b=(temp|b)&temp


#same question using dictionaries
d={}
d['a']=1
d['b']=2
print(d['a'])
a=d['b']
b=d['a']
print(a,b)

#problem using iter tool
import itertools
gen=iter([1,2,3])
lst=list(gen)
lst[0],lst[1]=lst[1],lst[0]
print(lst)
"""

"""
#print(6>>+2)
"""

print(1//2)
print(5//2)