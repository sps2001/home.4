#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1. First and Last digit 
num=int(input("Enter the number "))
def a(num):
    while(num>=10):
        num=num/10
    return int(num)
def z(num):
        num=num%10
        return num
print("The first digit in the number is",a(num),"The last digit in the number is",z(num))       


# In[ ]:


#2. Fibonacci Numbers
n=int(input("Length of Fibonacci Series ")) 
a = 0
b = 1
count = 0
if(n<=0): 
     print("Error") 
elif(n == 1): 
    print(a) 
else:  
    print("The fibonacci series is") 
    while count < n:
        print(a)
        c = a + b
        a = b
        b = c
        count = count + 1  


# In[ ]:


#3. Marks of Students
n = int(input("Enter number of students "))
if(n>=0):
    student=["member"]
    for i in range(0,n):
        name=input('Enter the name of student ')
        print(name)
        mark=int(input('Enter the marks out of 100 '))
        print(mark)
        if(mark<40):
            student.append(name)
            print("This student has failed")
        else:
            print("You have passed")
    for i in range(1,len(student)):
        print(student[i])
else:
    print("Invalid input")


# In[ ]:


#4. Multiplication Table
n=int(input("Which multiplication table do you want? "))
for i in range(1, 11):
   print(n, 'x', i, '=', n*i)


# In[ ]:


#5. Taking number
sum=0
c=0
num=int(input("Enter the number"))
while num!=-1:
    c+=1
    sum+=num
    num=int(input())
print(sum/c)


# In[ ]:




