#
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# n=int(input("n:"))
# val=1
# for i in range(n):
#     for j in range(n):
#         if i>=j:
#             print(val,end=" ")
#         else:
#             print(" ",end=" ")
#     print()
#     val+=1

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# n=int(input("n:"))
# for i in range(n):
#     val=1
#     for j in range(n):
#         if i>=j:
#             print(val,end=" ")
#         else:
#             print(" ",end=" ")
#         val+=1
#     print()


# 4
# 3 3
# 2 2 2
# 1 1 1 1
# n=int(input("n:"))
# val=n
# for i in range(n):
#     for j in range(n):
#         if i>=j:
#             print(val,end=" ")
#         else:
#             print(" ",end=" ")
#     print()
#     val-=1

# 4
# 4 3
# 4 3 2
# 4 3 2 1
# n=int(input("n:"))
# for i in range(n):
#     val=n
#     for j in range(n):
#         if i>=j:
#             print(val,end=" ")
#         else:
#             print(" ",end=" ")
#         val-=1
#     print()


# 1 2 3 4
#   1 2 3
#     1 2
#       1

# n=int(input("n:"))
# for i in range(n):
#     val=1
#     for j in range(n):
#         if i<=j:
#             print(val,end=" ")
#             val+=1
#         else:
#             print(" ",end=" ")
#     print()



# 1 1 1 1
#   2 2 2
#     3 3
#       4

# n=int(input("n:"))
# val=1
# for i in range(n):
#     for j in range(n):
#         if i<=j:
#             print(val,end=" ")
#         else:
#             print(" ",end=" ")
#     print()
#     val+=1


# 4 4 4 4
#   3 3 3
#     2 2
#       1

# n=int(input("n:"))
# val=n
# for i in range(n):
#     for j in range(n):
#         if i<=j:
#             print(val,end=" ")
#         else:
#             print(" ",end=" ")
#     print()
#     val-=1

#       1
#     2 2
#   3 3 3
# 4 4 4 4

# n=int(input("n: "))
# val=1
# for i in range(n):
#     for j in range(n):
#         if i+j>=n-1:
#             print(val,end=" ")
#         else:
#             print(" ",end=" ")
#     print()
#     val+=1

# 1 1 1 1
# 2 2 2
# 3 3
# 4
# n=int(input("n: "))
# val=1
# for i in range(n):
#     for j in range(n):
#         if i+j<=n-1:
#             print(val,end=" ")
#         else:
#             print(" ",end=" ")
#     print()
#     val+=1



# 4 4 4 4
# 3 3 3
# 2 2
# 1
# n=int(input("n: "))
# val=n
# for i in range(n):
#     for j in range(n):
#         if i+j<=n-1:
#             print(val,end=" ")
#         else:
#             print(" ",end=" ")
#     print()
#     val-=1


# 1 2 3 4
# 1 2 3
# 1 2
# 1
# n=int(input("n: "))
# for i in range(n):
#     val=1
#     for j in range(n):
#         if i+j<=n-1:
#             print(val,end=" ")
#         else:
#             print(" ",end=" ")
#         val+=1
#     print()


# 4 3 2 1
# 4 3 2
# 4 3
# 4
# n=int(input("n: "))
# for i in range(n):
#     val=n
#     for j in range(n):
#         if i+j<=n-1:
#             print(val,end=" ")
#         else:
#             print(" ",end=" ")
#         val-=1
#     print()
    
    


# 1 2 3 4
# 5 6 7 8
# 9 10 11 12
# 13 14 15 16

# n=int(input("n: "))
# val=1
# for i in range(n):
#     for j in range(n):
#         print(val,end=" ")
#         val+=1
#     print()


# 001 005 009 013
# 002 006 010 014
# 003 007 011 015
# 004 008 012 016

# n=int(input("n: "))
# val = 1
# for i in range(n):
#     for j in range(n):
#         print(str(val).zfill(3), end=" ")
#         val += 4
#     val = val-4*n+1
#     print()


# 1 $ $ $
# * 2 $ $
# * * 3 $
# * * * 4
# n=int(input("n: "))
# val=1
# for i in range(n):
#     for j in range(n):
#         if i==j:
#             print(val,end=" ")
#         elif i<=j:
#             print("$",end=" ")
#         else:
#             print("*",end=" ")
#     print()
#     val+=1
