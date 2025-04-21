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



#nivensnumber
n=156
sum=0
while(n>0):
    n1=n%10
    sum+=n1
    n=n//10
if n%sum==0:
    print('yes')
else:
    print('no')


#Happynumber
num=int(input("Enter a number: "))
visit=set()
while num!=1 and num not in visit:
    visit.add(num)
    sum=0
    temp=num
    while temp>0:
        d=temp%10
        sum+=d**2
        temp//=10
    num=sum
if num==1:
    print("Happy")
else:
    print("Unhappy")
'''

