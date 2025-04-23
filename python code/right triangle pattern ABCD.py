# A
# B B
# C C C
# D D D D

# n=int(input("n:"))
# char=input("char:")
# val=ord(char)
# for i in range(n):
#     for j in range(n):
#         if i>=j:
#             print(chr(val),end=" ")
#         else:
#             print(" ",end=" ")
#     print()
#     val+=1  


# A
# A B
# A B C
# A B C D

# n=int(input("n:"))
# char=input("char:")
# for i in range(n):
#     val=ord(char)
#     for j in range(n):
#         if i>=j:
#             print(chr(val),end=" ")
#         else:
#             print(" ",end=" ")
#         val+=1  
#     print()
    

# D
# C C
# B B B
# A A A A

# n=int(input("n:"))
# char=input("char:")
# val=ord(char)
# for i in range(n):
#     for j in range(n):
#         if i>=j:
#             print(chr(val),end=" ")
#         else:
#             print(" ",end=" ")
#     print()
#     val-=1  


# D D D D
#   C C C
#     B B
#       A

# n=int(input("n: "))
# char=input("char: ")
# val=ord(char)
# for i in range(n):
#     for j in range(n):
#         if i<=j:
#             print(chr(val),end=" ")
#         else:
#             print(" ",end=" ")
#     print()
#     val-=1




# D C B A
#   D C B
#     D C
#       D

# n=int(input("n:"))
# char=input("char: ")
# for i in range(n):
#     val=ord(char)
#     for j in range(n):
#         if i<=j:
#             print(chr(val),end=" ")
#             val-=1
#         else:
#             print(" ",end=" ")
#     print()


#       A
#     B B
#   C C C
# D D D D

# n=int(input("n:"))
# char=input("char: ")
# val=ord(char)
# for i in range(n):
#     for j in range(n):
#         if i+j>=n-1:
#             print(chr(val),end=" ")
#         else:
#             print(" ",end=" ")
#     print()
#     val+=1




#       D
#     D C
#   D C B
# D C B A

# n=int(input("n:"))
# char=input("char: ")
# for i in range(n):
#     val=ord(char)
#     for j in range(n):
#         if i+j>=n-1:
#             print(chr(val),end=" ")
#             val-=1
#         else:
#             print(" ",end=" ")
#     print()
   
#       D
#     C C
#   B B B
# A A A A

# n=int(input("n: "))
# char=input("char: ")
# val=ord(char)
# for i in range(n):
#     for j in range(n):
#         if i+j>=n-1:
#             print(chr(val),end=" ")
#         else:
#             print(" ",end=" ")
#     print()
#     val-=1



# A B C D
# A B C
# A B
# A
# n=int(input("n:"))
# char=input("char: ")
# for i in range(n): 
#         val=ord(char)
#         for j in range(n):
#             if i+j<=n-1:
#                 print(chr(val),end=" ")
#                 val+=1
#             else:
#                 print(" ",end=" ")
#         print()



# D C B A
# D C B
# D C
# D
# n=int(input("n:"))
# char=input("char: ")
# for i in range(n): 
#         val=ord(char)
#         for j in range(n):
#             if i+j<=n-1:
#                 print(chr(val),end=" ")
#                 val-=1
#             else:
#                 print(" ",end=" ")
#         print()


# A A A A
# B B B
# C C
# D               
# n=int(input("n: "))
# char=input("char: ")
# val=ord(char)
# for i in range(n): 
#     for j in range(n):
#         if i+j<=n-1:
#             print(chr(val),end=" ")
#         else:
#             print(" ",end=" ")
#     print()
#     val+=1





# D D D D
# C C C
# B B
# A
# n=int(input("n: "))
# char=input("char: ")
# val=ord(char)
# for i in range(n): 
#     for j in range(n):
#         if i+j<=n-1:
#             print(chr(val),end=" ")
#         else:
#             print(" ",end=" ")

#     print()
#     val-=1