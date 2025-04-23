l=['tea','ate','abc','bac','xyz','zyx']
d={}
for i in l:
    key="".join(sorted(i))
    if key not in d:
        d[key]=[]
        # print(d)
    d[key]+=[i]
    print(d)
print(list(d.values()))


'''------------------------------------------------------------------'''

l=[1,2,3,4,5,6]
res=[]
target=7
for i in l:
    for j in l:
        if i+j==target:
            res+=[(i,j)]
print(res)

'''[(1, 6), (2, 5), (3, 4), (4, 3), (5, 2), (6, 1)]'''

'''-------------------------------------------'''

l=[1,2,3,4,5,6,6,1]
res=[]
target=7
for i in l:
    for j in l:
        if i+j==target and  (i,j)not in res:
            res+=[(i,j)]
print(res)
'''
[(1, 6), (1, 6), (2, 5), (3, 4), (4, 3), (5, 2), (6, 1), (6, 1), (1, 6), (1, 6), (6, 1), (6, 1)] 
to avoid this we added  (i,j) not in condition'''
'''[(1, 6), (2, 5), (3, 4), (4, 3), (5, 2), (6, 1)]'''

'''---------------------------------------------------------------------'''


'''for hetrogenous list '''

l=[1,2,3,4,5,6,'hi']
res=[]
target=7
for i in l:
    for j in l:
        if type(i)==int and type(j)==int and i+j==target and (i,j)not in res :
            res+=[(i,j)]
print(res)
'''[(1, 6), (2, 5), (3, 4), (4, 3), (5, 2), (6, 1)]'''



l=[-1,2,1,1,3,-2]
res=[]
target=0
for i in l:
    for j in l:
        for k in l:
            if i+j+k==target and (i,j,k) not in res :
                res+=[(i,j,k)]
print(res)

''' [(-1, -1, 2), (-1, 2, -1), (-1, 3, -2), (-1, -2, 3), (2, -1, -1),
  (1, 1, -2), (1, -2, 1), (3, -1, -2), (3, -2, -1), (-2, -1, 3), (-2, 1, 1), (-2, 3, -1)]'''



# l1=[]
# i=3
# j=6
# l1+=[(i,j)]
# print(l1)



result=print
result("Hi")
r="hello$"
cr=r.encode(encoding='ascii',errors='replace')
cr=cr.decode()
for i in cr:
    print(i)

'''Hi
h
e
l
l
o
$'''



# s='1'
# s1="%"
# print()
# print("isdigit",s.isdigit)
# print("isdigit",s1.isdigit)
# print("isnumeric",s.isnumeric)
# print("isnumeric",s1.isnumeric)
'''why ??????????????????????????????'''
'''
isdigit <built-in method isdigit of str object at 0x000001fbd683e2f0>
isdigit <built-in method isdigit of str object at 0x000001fbd6c015b0>
isnumeric <built-in method isnumeric of str object at 0x000001fbd683e2f0>
isnumeric <built-in method isnumeric of str object at 0x000001fbd6c015b0>'''

# l=[19,10,15,17,20]

n=int(input("N:"))
st=str(n)
even=[]
odd=[]
for i in st:
    if int(i)%2==0:
        even.append(i)
    else:
        odd.append(i)
res="".join(even+odd)
print(res)

# N:897634521
# 864297351


n=input("n:")
if n==n[::-1]:
    print(f"{n} is a palindrome")
else:
    print(f"{n}is not a palindrome")

# n:DANA
# DANAis not a palindrome
# n:malayalam
# malayalam is a palindrome

n=int(input("N:"))
res=str(n)[::-1]
print(int(res))

# N:78901
# 10987

n=int(input("N:"))
sum=0
temp=n
while temp<0:
    fact=1
    rem=temp%10
    for i in range(1,rem+1):
        fact*=i
        sum+=fact
        temp//=10
    if sum==n:
        print("strong number")
    else:
        print("not strong number")
    