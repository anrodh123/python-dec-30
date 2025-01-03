#wap even or odd
'''num=int(input("Enter a number:"))
if num%2==0:
#    print("the number is even")
    print("{} is even".format(num))
else:
#    print("the number is odd") 
    print("{} is odd".format(num))   '''
#--------------------------------------
'''num=int(input("Enter a number:"))
if num%2==0:
   
    print("{} is even".format(num**2))
else:

    print("{} is odd".format(num**2)) '''  
#-----------------------------------------------------
'''n=[1,2,3,4,5,6,7,8,9]
odd_sq=[]
even_sq=[]
for i in n:
    if i%2==0:
      even_sq.append(i**2)
    else:
      odd_sq.append(i**2)
print(f"{n} even is {even_sq},  odd is {odd_sq}")  ''' 
#----------------------------------------------
#wap  square and cube
'''n=[2,3,4,5,6]
for i in n:
   print(f"{i} square is {i**2}, and {i} cube is {i**3}")'''
#-----------------------------------------------------
#wap grade mark  
'''num=int(input("enter a mark:"))
if num>=90 and num<=100:
    print("your grade is A1")
elif num>=80 and num<90:
    print("your grade is A2")
elif num>=70 and num<80:
    print("your Grade is B1")
elif num>=60 and num<70:
    print("your Grade is B2")  
elif num>=50 and num<60:
    print("your Grade is C")    
else:
    print("Fail students")    '''  
#----------------------------------------
#wap factorial
'''num=int(input("enter a number:"))
fact=1
if num==0:
    print("factorial of enter number {} is {}".format(num,fact))
else:
    for i in range(1, num+1):
        fact*=i
    print("factorial of enter number {} is {}".format(num,fact)) '''   
#-----------------------------------------------------------------------
#wap multiplication table
'''num=int(input("enter a number:"))
for i in range(1,11):
    print("{}*{}={}".format(num,i,(num*i)))'''
#-------------------------------------------------------
#wap prime number or not
'''num=int(input("enter a number:"))
count=0
for i in range(1, num+1):
    if num%i==0:
        count +=1
if count==2:
    print(num,"is prime number")
else:
    print(num,"is not prime number")    '''
#--------------------------------------------
'''num=int(input("enter a number:"))
if num==1:
    print("is not prime number")
if num>1:    
    for i in range(2,num):
        if num%2==0:
            print(num,"is not prime number")
            break
else:
   print(num,"is prime number")'''
#------------------------------------------------------
'''num=int(input("enter a number:"))
flag=False
for i in range(2,num):
    if num%i==0:
        flag=True
        break
if flag:
    print("enter number {} is not prime".format(num))
else:
    print("enter number {} is  prime".format(num)) '''
#-------------------------------------------------
# #wap swap two numbe and tree
'''num1=int(input("enter a number:"))
num2=int(input("enter a number:"))  
#print("Before swapping num1={} and num2={}".format(num1,num2))   
print(f"Before swapping num1={num1} and num2={num2}") 
temp=num1
num1=num2
num2=temp
print(f"After swapping num1={num1} and num2={num2}") '''
#-----------------------------------------------------------
#wap armstrong or not
'''num=int(input("enter a number:"))
sum=0
for i in range(num):
    sum+=i**3
if sum==num:
    print("armstrong")   
else:
    print("not armstrong")     '''
#wap count number of digits in integer
num=int(input("enter a number:"))
count=0
while num!=0:
    num=num//10
    count+=1
print("number of digit in given number is",count)