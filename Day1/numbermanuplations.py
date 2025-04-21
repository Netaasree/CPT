'''
#number manuplations in python
1.arm strong
2.strong number same as krishnamurthy's number
4.nivens number same as harsads
6.happy
7.atomorphic
8.adam's
9.magic
'''
#Strong 
num=145
copy=num
sum=0
while(num>0):
    n1=num%10
    mul=1
    for i in range(1,n1+1):
        mul=mul*i
    sum+=mul
    num//=10
if sum==copy:
    print("success")
else:
    print("Fail")

