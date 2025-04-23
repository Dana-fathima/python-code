'''4 * 3 * 2
   4 * 3 * 2
   4 * 3 * 2
   4 * 3 * 2'''
#row=int(input("row:"))
#col=int(input("column:"))
#for i in range (row):
#    val=row
#    for j in range(col):
#        if j%2==0:
#            print(val,end=" ")
#            if j%2==0:
#                val-=1
#        else:
#            print("*",end=" ")
#    print()


'''A * B *
   A * B *
   A * B *
   A * B * '''

#n=int(input("n:"))
#for i in range(n):
#    val=ord("A")
#    for j in range(n):
#        if j%2==0:
#            print(chr(val),end=" ")
#            if j%2==0:
#                val+=1
#        else:
#            print("*",end=" ")
#    print()        
        

'''  E E E E
     D D D D
     C C C C 
     B B B B
     A A A A'''

#row=int(input("row:"))
#col=int(input("column:"))
#n=input("char:")
#val=ord(n)
#for i in range(row):
#    for j in range(col):
#        print(chr(val),end=" ")
#    print()
#    val-=1


'''D D D D
   4 4 4 4
   C C C C
   3 3 3 3'''

n=int(input("n:"))
ch=input("char:")
no=int(input("no. to start:"))
val=ord(ch)
val1=no
for i in range(n):
    for j in range(n):
        if i%2==0:
            print(chr(val),end=" ")
        else:
            print(val1,end=" ")
    print()                    
    if i%2==0:
        val-=1
    if i%2!=0:
        val1-=1  