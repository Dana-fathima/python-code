# A * B * C
# * D * E *
# F * G * H
# * I * J *
# K * L * M

# n=int(input("n: "))
# char=input("char: ")
# val=ord(char)
# for i in range(n):
#     for j in range(n):
#         if (i+j)%2==0:
#             print(chr(val),end=" ")
#             val+=1
#         else:
#             print("*",end=" ")
#     print()
        
# n=int(input("n: "))
# val=1
# for i in range(n):
#     for j in range(n):
#         if i>=j:
#             if i%2==0:
#                 print(val,end=" ")
#             else:
#                 print("*",end=" ")
#         val+=1
#     print()
#     val+=1




#       A
#     B A
#   C B A 
# D C B A

# n=int(input("n:"))
# char= input("char:")
# for i in range(n):
#     val = ord(char)
#     for j in range(n):
#         if i+j>=n-1:
#             print(chr(val),end=" ")   
#         else:
#             print(" ",end=" ")
#         val-=1
#     print()
  

# n=int(input("n: "))
# for i in range(n):
#     val=1
#     for j in range(n):
#         if val<100:
#             print(str(val).zfill(3),end=" ")
#             val+=1
#         else:
#             print(val,end=" ")
#             val=+1
#     print()
  


# n = int(input("Enter n: "))
# val = 1
# for i in range(n):
#     for j in range(n):
#         print(str(val).zfill(3), end=" ")
#         val += 4
#     val = val - 4 * n + 1
#     print()


#       *
#     * *
#   *   *
# *     *
#   *   *
#     * *
#       *

# n=int(input("n: "))
# for i in range(2*n-1):
#     for j in range(n):
#         if j==n-1 or i+j==n-1 or i-j==n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()






#     *
#     *
# * * * * *
#     *
#     *

# n=int(input("n: "))
# for i in range(n):
#     for j in range(n):
#         if i==n//2 or j==n//2:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()