# 1
#   2
#     3
#       4

# n=int(input("n:"))
# for i in range(n):
#     val=1
#     for j in range(n):
#         if i==j:
#             print(val,end=" ")
#         else:
#             print(" ",end=" ")
#         val+=1
#     print()
  


# A
#   B
#     C
#       D
# n=int(input("n:"))
# char=input("char:")
# for i in range(n):
#     val=ord(char)
#     for j in range(n):
#         if i==j:
#             print(chr(val),end=" ")
#         else:
#             print(" ",end=" ")
#         val+=1  
#     print()
    


# D
#   C
#     B
#       A
# n=int(input("n:"))
# char=input("char:")
# for i in range(n):
#     val=ord(char)
#     for j in range(n):
#         if i==j:
#             print(chr(val),end=" ")
#         else:
#             print(" ",end=" ")
#         val-=1  
#     print()



# 4
#   3
#     2
#       1

# n=int(input("n:"))
# for i in range(n):
#     val=n
#     for j in range(n):
#         if i==j:
#             print(val,end=" ")
#         else:
#             print(" ",end=" ")
#         val-=1
#     print()




#       1
#     2
#   3
# 4

# n=int(input("n: "))
# val=1
# for i in range(n):
#     for j in range(n):
#         if i+j==n-1:
#             print(val,end=" ")
#         else: 
#             print(" ",end=" ")
#     print()
#     val+=1



#       A
#     B
#   C
# D

# n=int(input("n: "))
# char=input("char: ")
# val=ord(char)
# for i in range(n):
#     for j in range(n):
#         if i+j==n-1:
#             print(chr(val),end=" ")
#         else:
#             print(" ",end=" ")
#     print()
#     val+=1

#       D
#     C
#   B
# A
# n=int(input("n: "))
# char=input("char: ")
# val=ord(char)
# for i in range(n):
#     for j in range(n):
#         if i+j==n-1:
#             print(chr(val),end=" ")
#         else:
#             print(" ",end=" ")
#     print()
#     val-=1


#      4
#     3
#   2

# 1
# n=int(input("n: "))
# val=n
# for i in range(n):
#     for j in range(n):
#         if i+j==n-1:
#             print(val,end=" ")
#         else: 
#             print(" ",end=" ")
#     print()
#     val-=1


# n=int(input("n: "))
# for i in range(n):
#     for j in range(n):
#         if i+j==n//2 or j-i==n//2 or i-j==n//2 or i+j==n+n//2-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


# A
# A B
# A B C
# A B C D

# n=int(input("n: "))
# char=input("char: ")
# for i in range(n):
#     val=ord(char)
#     for j in range(n):
#         if i>=j:
#             print(chr(val),end=" ")
#         val+=1
#     print()


# A
#   *
#     B
#       *
# n=int(input("n:"))
# char=input("char: ")
# val=ord(char)
# for i in range(n):
#     for j in range(n):
#         if i==j:
#             if i%2==0:
#                 print(chr(val),end=" ")
#                 val+=1
#             else:
#                 print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()  
              

# 1 1 1 1
#   * * *
#     2 2
#       *

# n=int(input("n: "))
# val=1
# for i in range(n):
#     for j in range(n):
#         if i<=j:
#             if i%2==0:
#                 print(val,end=" ")
#             else:
#                 print("*",end=" ")
#         else:
#             print(" ",end=" ") 
#     print()
#     if i%2==0:
#         val+=1

# * 1 * 2
# * 3 * 4
# * 5 * 6
# * 7 * 8

# n=int(input("n: "))
# val=1
# for i in range(n):
#     for j in range(n):
#         if j%2==0:
#             print("*",end=" ")        
#         else:
#             print(val,end=" ")
#             val+=1
#     print()
