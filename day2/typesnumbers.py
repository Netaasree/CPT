'''
term=int(input("Enter the term value: "))
value=0
for i in range(1,term+1):
    if i%2==0:
        value=((i//2)-1)*7
    else:
        value=(i//2)*6
print("The",term,"th value is",value)
'''

'''
num=int(input("Enter the term value: "))
a,b=0,0
for i in range(1,num+1):
    if i%2!=0:
        a+=7
    else:
        b+=6
if num%2!=0:
    print("{} term of series is {}".format(num,a-7))
else:
    print("{} term of series is {}".format(num,b-6))
'''

#given sequence 1 1 2 3 4 9 16 27 ....... nth terms
num=int(input("Enter the term value: "))
if num%2==1:
    print(2**(num//2))
else:
    print(3**(num//2-1))
