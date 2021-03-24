#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1.What are the two values of the Boolean data type? How do you write them?

print("The two values are 1)True(1) & 2) False(0) . ")


# In[2]:


#2. What are the three different types of Boolean operators?

print("AND ,OR, NOT. are the three different boolean operators")


# In[3]:


#3. Make a list of each Boolean operator's truth tables (i.e. every possible combination of Boolean values for the operator and what it evaluate .)



print()
print("'A','AND','B','evaluation'")
AND=[[1,1,1],
  [1,0,0],
  [0,1,0],
  [0,0,0]]
print('AND:',AND)

print()
print("'A','OR','B','evaluation'")
OR=[[1,1,1],
  [1,0,1],
  [0,1,1],
  [0,0,0]]
print('OR:',OR)

print()
print("'A','not','evaluation'")
ANOT=[[1,0],
  [0,1]]
print('ANOT:',ANOT)

print()
print("'B','not','evaluation'")
BNOT=[[1,0],
  [0,1]]
print('BNOT:',BNOT)


# In[4]:


#4. What are the values of the following expressions?
a=(5 > 4) and (3 == 5)
b=not (5 > 4)
c=(5 > 4) or (3 == 5)
d=not ((5 > 4) or (3 == 5))
e=(True and True) and (True == False)
f=(not False) or (not True)

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)


# In[5]:


#5. What are the six comparison operators?



print(" the  comparison operators are : 1)less than(<),2)greather then(>),3)equal to(==),4)not equal to(!=),5)grether then or equal to(>=),6)less then or equal to(<=)")


print()
a=int(input("enter the first element"))
b=int(input("enter the second element"))
print("a<b",a<b)
print("a>b",a>b)
print("a==b",a==b)
print("a!=b",a!=b)
print("a>=b",a>=b)
print("a<=b",a<=b)


# In[6]:


#6. How do you tell the difference between the equal to and assignment operators?Describe a condition and when you would use one.


print("'==' means equal(comparision operator) and '= ' is assignment operator. The assignment operator is use to siign the value to the variable .  And comparision operator is use to  comparing to values which is stored in variable")
print(" to assign the value to the variable use assignment operator and to comparining to values use comparision operator.")
print()


# In[7]:


#7. Identify the three blocks in this code:
spam = 0
if spam == 10:
    print("eggs")
if spam > 5:
    print("bacon")
else:
    print("ham")
    print("spam")
    print("spam")
    
    
    
print()
print()
print("three blocks are :")
 #first if part is our first block
print("1) if spam == 10 print('eggs')")

      
 #second  if part is our second block
      
print("2)if spam > 5: print('bacon')")
print()
#else part is our third block
print("3 )else: print('ham')print('spam') print('spam'))")


# In[8]:


#8. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.

a=int(input("enter the any number:"))


if a==1:
    print("Hello")
    
elif a==2:
    print("Howdy")
    
else:
    print("Greetings!")


# In[9]:


#9.If your programme is stuck in an endless loop, what keys you’ll press?

print("press 'CTRL+C'")


# In[10]:


#10. How can you tell the difference between break and continue?


print("break statement	                                 continue statement")
print("It causes early termination of a loop.	        It causes early execution of the next task")
print("break stops the continuation of the loop.	     continuation of loop. continue do not stop the continuation ")

print("                                                   of the loop,it will only stop the current statement")


# In[11]:


#11. In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?


print("the out of three renge functions  are same ,only tiping difference. in 1 range function the only mention the end of the program but starting by0 and stepsize is bydefault 1" )
for i in range(10):
    print(i)
print()
for j in range(0,10):
    print(j)
print()
    
for k in range (0,10,1):
    print(k)


# In[12]:


#12. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.


print("using for loop:")

for i in range(1,10,1):
    print(i)
print()
print("using while loop:")

i=0
while (i<10):
    print(i)
    i=i+1


# In[13]:


#13. If you had a function named bacon() inside a module named spam, how would you call it after importing spam?
print("import spam as s")
# by using alias name we can call the function which is inside the module 
print("s.bacon()")


# In[ ]:




