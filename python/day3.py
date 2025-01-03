'''age=30
member=True
if age>18:
    if member:
        print("ticket $12")
    else:
          print("ticket $12")  
else:
print("ticket $12")  '''    
#-----------------------

'''for i in "sudan":
    print(i)   '''

'''for in "broadway":
 print(i)'''

a="Broadway"
print(a[0])   



for i in range(2,11,2):
    print(i)    

for i in range(1,11,1):
    if i==5:
        continue
    print(i)
else:
    print("loop complete")


data="hello"
for i in range(0,len(data),1): 
    print(data[i])   
#-------------------------------------------
num=int(input("enter a number:"))
for i in range(1,11):
    print("{}*{}={}".format(num,i,(num*i)))
#----------------------------------------
for i in range(1,11,1):
   a=f'2 x {i}={2*i}'
print(a)
#-------------------------------
for i in range(1,3):
    for a in range(1,4):
        print(a)
#------------------------------

for i in range(1, 6):
 for j in range(1, i+1):
    print(j, end=" ")
    
 print("")        