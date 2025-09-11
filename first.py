# print("hello world !")
# print("enter your name :")
# hello =input()
# print(hello,"bonjur")
# name="shubham"

# print(hello,"bonjur"+name)

# comaprision operators 
# >
# >
# !
# <=s
# >=

# logical operator 
# if(not 10 > 20):
#     print(True)
# else:
#     print(False)
# print sum 
# num1 =int(input("enter num first:"))
# num2 =int(input("enter num second:"))
# print("sum is :",num1+num2)
# side= float(input("enter side of square:"))
# print("area :",side*side)
#  print average of two number
# num1= float(input("enter num1"))
# num2= float(input("enter num2"))
# print("average is :",(num1+num1)/2)
# # idx in strings 

# str="hello world"
# str="yoo"
# print(str[ :])
# str1= str[4:7]
# print(str1)
# print(str)

# wap to input user name and its length  
# Fname=input("enter your first name: ")
# print("and this is your name length: ",len(Fname))

# wap to find $ in string 
# stri ="aug$dudhd#$^"
# print(stri.count("$"))

# use of nesting in python 
# sal= int(input("enter ur salary"))
# age= int(input("enter ur age"))
# ep= int(input("enter ur experince"))
 
# if(sal>50000):
#   print("first gate will open:")
#   if(ep>10):
#    print("second gate will open")
#    if(age>10):
#      print("finally u got bonus")
# else:
#   print("no-bouns")

# grade students based on there marks 

# marks >=90 g=A 
# marks >=80 g=B 
# marks >=70 g=C 
# marks <70 g=D  
 
# marks =int(input("enter your marks :"))
# if(marks>=90 and marks<=100):
#     print("your grade is A")
# elif(marks>=80 and marks<90):
#     print("your grade is B")
# elif(marks>=70 and marks<80):
#     print("your grade is C")    
# else:
#     print("ur grade is D")


# enterd number is even or odd 
# num= int(input("input the first number :"))
# num= int(input("input the second number :"))
# num= int(input("input the third  number :"))
# if(num%2==0):
#     print("number is even")
# else:
#     print("number is odd")

#find the biggest number 
# num1=10
# num2=23
# num3=30
# if(num1>num2 and num1>num3):
#     print(num1," is bigger the rest number")
# elif(num2>num1 and num2>num3):
#     print(num2," is bigger the rest number")
# else:
#     print(num3,"is bigger")


# list and tuples 
# slic=["shubh",22,23.44,"dehli"]
# print(slic[1:3])
# li=["hello",23,55.6]
# li.append("https")
# li.insert(4,"yarr")
# print(li)
# # checking it is mutable or not 
# li[2]="hdrg"
# print(li)
# yes list in python are mutable
 

#  tuples
# tuples are as same as list in python , but there are one main difference between both is tuples are immutable in python 
  
# tup=("weges",68,33.5, True)
# print(tup)
# # tup[1]="hello"  
# tup1=(1,)
# print(tup1)



# WAP to ask use to enter names of there 3 favorite movie and store in list  
#  

#  WAP to check the list contains a palidrome of element (hint  use copy method)
# list1= [1,2,3,2,1 ]
# list2= [1,"abc","abc",1]
# list1_copy=list1.copy()
# list1_copy.reverse()
# if(list1_copy==list1):
#     print("palidrome")
# else:
#     print("not palidrome")

# list2_copy=list2.copy()
# list2_copy.reverse()
# if(list2_copy==list2):
#     print("palidrome")
# else:
#     print("not palidrome")

# count function in tuple
# WAP in python to show the use of tuple

# tup= ("A","b","c","A","A","d","A","c",)
# print("count of A is :",tup.count("A"))


# dictionary in python :

# dic={
#     "greet": "hello",
#     "name":"shubham",
#    "last_N": "acharya",
# }
# print(dic["greet"])

# dic={
#     "greet": "hello",
#     "M-num":6374,
#     "12class":["shubham","11",760,323233],
#     "11class":("arpan","12",780,3233),
#    "last_Y": True,
#    "new_dic": {
#        "greet": "bonjur",
#     "M-num":6365,
#     "10class":["khushi","10",820,233],
#    }
# }
# print(dic["11class"][2])
# print(dic["new_dic"]["10class"][0])
# dic["new_dic"]["origin"]="fance"      # assiging the key valuse pair in dictionary 
# print(dic["new_dic"])


# set in python 

# set is collection immutable data 
# in set we store data like str,int , boolean, float, tuples, bcoz these data type are inmutable 
# set are unorderd in python 

# set1={ 1,2,3,4,5,6,3,1,"hello","hello","yoo",234.4}
# print(set1,type(set1))

# Q store a following word meaning in python dictionary 
# table: a piece of furniture , list of fact and figures
# dic={
# }
# dic["cat"]="a small animal"
# dic["table"]=("a piece of furniture ","list of fact and figures")
# # dic["table"]=["a piece of furniture ","list of fact and figures"]
# print(type(dic["table"]))
# print(dic)
# print(dic["table"][0])

# Q you are given a list of subject for student assume one classroom is required for 1 subject how many classrooms are needed by all student 

# set1={"python","java","C++","python","javascript","java","python","java","C++","c" }
# print(len(set1))


# this two lines will print all the word 
# import keyword
# print(keyword.kwlist)

# loops 
# pe=0
# while(pe<10):
#     print("hello")
#     pe=pe+1

# j=13; com=2+12j
# print(com)


# if(input("enter the username :")=="campusX" and int(input("enter the password :"))==123):
#     print("welcome")
# else:
#     print("wrong password")

# for(i=0;i<10;):
#   print("hello")
# i=0
# while(i<10):
#     print("hello")
#     i+=1


# here we are creating the number guessing game in pythons 
# import random
# random_num=random.randint(20,30)
# print(random_num)
# attampt_count=None
# user_num=int(input("enter the number"))
# attampt_count =+1
# if(random_num==user_num):
#     print("yehhh rigth guesss !!")
#     print("u took ",attampt_count," to guess the number !")
# else:
#     while(True):
#          user_num=int(input())
#          attampt_count+=1
#          if(random_num==user_num):
#            print("yehhh rigth guesss !!")
#            print("u took ",attampt_count," to guess the number !")
#            break
# li =["hello","namaste","yoo","hola","good morning"]
# for i in li:
#     print(i)
# for i in range(12):
#     print(i)

# li ={
#     " he":"hello",
#     "yo":"name",
#     "namaste":"yoo",
# }
# for i in li:
#     print(li[i])

# nested loop
# for i in range(1,5):
#     for j in range(0,i):
#         print("*", end="") 
#     print()

# *
# **
# ***
# ****
# *****
# ******
# *******
# ********
# *********

# start=int(input("enter number of row :"))
# for i in range(1,start):
#     for j in range(0,i):
#         print("*", end="") 
#     print()

# pass statement in python 
# 
# pass statemnet simplly pass(help to move in next line without writing the current loop logic)
# just like this 

# for i in range():
#     pass  # no need to write the current logic 
# print("hello")
# print("TI")
# see we can write code without writing the logic in loop   


# built-in function
# print("hello")
# input("enter your input ")
# print(type(12)) # to define data type oof values 
# int()
# float()
# bool()
# set()
# list()
# tuple()
# print(abs(15.44))  #print only absolute values 
# print(pow(2,3)) #which means 2 the power 3
#min/max 
# print(min([1,2,3,4,5,6,8])) # it will find the minimun value in list,tuple,set, or series type data 
# print(min([1,2,3,4,5,6,8])) # it will find the maximun value in list,tuple,set  or series type data 
# print(round(23.88454,3)) # it will give the round soff the number
# help function 
# help function give us the details of any funtion
# help()


# built-in module 
# it will show all in modules in my pc 
# help("modules")

# help(print) 
# import time
# tem =time.time()
# tem/=60
# print(tem/60)
# print(time.ctime())
# print("hello")
# print(time.sleep(3))  # it work as delay() function in js
# print("yoo")
#
# li=[1,2,3,4,5,6]
# print(li[::-1])
# li1=[1,2,3,4,5,[6,7,[1,2]]]
# print(li1[5][2][1])
# li=[[[1,2],[3,4]],[[5,6],[7,8]]]
# print(li[1][1][0])

# mail="advgzvdbc@gmail"
# li=mail.split("@")
# print(li[0])    
# input [1,1,2,2,3,3,4]
# output [1,2,3,4]
# li =[1,2,3,3,4,4,445,224,3,3,4,5]
# li=set(li)
# print(list(li))
# tup=(1,2,3,4,5)
# print(tup)
# for i in tup:
#     print(i)
# print(tup[0])
# tup[0]="hello" #tuple are immutable 
# t=(1,2,3,4,(5,6))
# print(t[-1][-1]) 
# print(t)
# se={1,"hello",'a',(1,2)}
# print(type(se)) 
# help(dict)

# function in python
# def Phello():

#     print("hello")
#     return 0
# Phello()

# odd even function
# def OandE (i):
#     if(i%2==0):
#         print("number is even")
#     else:
#         print("number is odd")
#     return 0
# for i in range(0,10):
#   print(i, sep=" ")
#   OandE(i)

# def f(x):
#     x=x+1
#     print('in f(x):x =',x)
#     return x
# x=3
# z=f(x)
# def g(x):
#     def h(x):
#         x=x+1
#         print('in h(x):x =',x)
#     x=x+1
#     print('in g(x):x =',x)
#     h(x)
#     return x

# def h(y):
#     global x
#     x +=1
# x=5
# h(x)
# print(x)

# it will create infinity calls, till the maximum limit reached # call back hell
# def f():
#     print("inside f")
#     def g():
#         print("inside g")
#         f()
#     g()
# f()

# Python Practice Problems

#User will input (3ages).Find the oldest one 
# age1=int(input("enter your first age: "));age2=int(input("enter your second age: "));age3=int(input("enter your third age: "))
# if(age1>age2 and age1>age3):
#     print("age first is big one:",age1)
# if(age2>age1 and age2>age3):
#     print("age second is big one:",age2)
# else:
#     print("age third is big one:",age3)

# Write a program that will convert celsius value to fahrenheit
# cel=int(input("enter the degree celsius :"))
# fer = (cel*1.8)+32
# print(cel,"degree celsius ="+" fahrenheit :",fer)
# (34°C × 9/5) + 32 = 93.2°F

# User will input (2numbers).Write a program to swap the numbers
# num1=int(input("enter the first 1 number :"))
# num2=int(input("enter the second 2 number :"))
# num3=num1
# del num1
# num1= num2
# del num2
# num2= num3
# del num3
# print(num1)
# print(num2)
# # 
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))

# num1, num2 = num2, num1

# print("After swapping:")
# print("First number:", num1)
# print("Second number:", num2)


# 4.Write a program that will give you the sum of 3 digits
# num1=int(input("enter the three digit number :"))
# num1=str(num1)
# print(num1)
# su =0
# for i in num1:
#     su= su + int(i)
# print(su)
# # chatgpt code 
# num = int(input("Enter a 3-digit number: "))

# d1 = num // 100          # first digit
# d2 = (num // 10) % 10    # second digit
# d3 = num % 10            # third digit

# sum_digits = d1 + d2 + d3
# print("The sum of digits is:", sum_digits)

# Write a program that will reverse a four digit number.Also it checks whether the reverse is true
# num1=input("enter the four digit number :")
# num1 = num1[::-1]
# print(num1)

# recursion 
# def rec(a,b):
#     if(b==1):
#         return a
#     else:
#         return a+rec(a,b-1)

# rec(4,5)    
# def fact(num):
#     if(num==1):
#         return num
#     else:
#         return num * fact(num-1)
# print(fact(5))

# def pali(st):
#       if(len(st)<=1):
#        print("palindrome")  
#       else:
#         if(st[0]==st[-1]):
#           pali(st[1:-1]) 
#         else:
#           print("not palindrome")    
     
# pali("madam")

# hof 
# map
# filter
# reduce 
# l=[1,2,3,4,5]
# add= 0
# def hello(nam):
#     if(nam%2==0):
#       global add
#       add=add+nam
# list(map(hello,l))
# print(add)
# l=[1,2,3,4,5]
# print(list(map(lambda x: f"even{x*2}" if x%2==0 else "odd",l)))   

# de={
# "student":["shubham","khushi","arpan"],
# "class":[12,3,14]
# }
# print(list( map(lambda x: print(x),de["student"])))

# l1=["apple","mango","papaya","orange"]
# print(list(filter(lambda x:x if x.count("e") else None ,l1)))

# l2=[x**2 for x in range(0,10)]
# print(l2)
# print(25 in l2)
# de={
#     1:1,
#     2:2,
#     3:"htllo"
# }
# li=print(de.keys())


#  class and objects are start from here 
# syntex

# class ClassName :
#  # code,datatype , function
#  what is the defference between function and methods 
#  function are the block of code which do some task 
#  method are just like the function, but there is main difference between them is the method are work with its class/ written inside of class  object not with globally
# class Xyz:  
#     def __init__(self):
#         print("hello") 

# ob=Xyz()
# ob1=Xyz()
# ob2=Xyz()

# see in the xyz class we won't call init fuction but, every time we create an object the init function run itself 


     
# class Myclass:
#   def __init__(self):
#       self.name=""
#   def pHello(shu):
#         print("hello",shu)


# import module file is store in python > lib  folder
# import mymodul
# mymodul.Xyz()

# class Atm:
#     def __init__(self):
#         self.pin=""
#         self.balance=0
           
#     def menu(self):
#         userChoice=int(input("""
#             hello, how would  you like to start ?
#             1. enter 1 to create pass 
#             2. enter 2 to deposit
#             3. enter 3 to withdraw 
#             4. enter 4 to check balance
#             5. enter 5 to exit                
#            """))
#         if(userChoice== 1):
#             self.createP()
#             print("create password !")
#         elif(userChoice==2):
#               self.addB()
#               print("deposit !")
#         elif(userChoice==3):
#               print("withdrow amount!")
#         elif(userChoice==4):
#               print("total balane!",self.balance)
#         else:
#               print("exit !")
#               exit()
#     def createP(self):
#             self.pin= int(input("enter your pin: "))
#             print("pin set")
#             self.menu()
#     def addB(self):
#             self.balance= int(input("enter amount to deposits: "))
#             print("amount deposit !")
#             self.menu()
#     def addB(self):
#             self.balance= int(input("enter amount to deposits: "))
#             print("amount deposit !") 
#             self.menu()    
# ob= Atm().menu()

# class My :
#     def __init__(self):
#         self.hello=" "
#     def pH(self):
#         print(self.hello)
# ob= My # temporary object bcoz we wont store it in any variable for long storage 
# print(ob)

# class Xya :
#     def __init__(self):
#          print(id(self))
# ob1=Xya()
# print(int(id(ob1)))
# ob2= Xya()
# print(int(id(ob2)))

# class Myclass:
#     def __init__(self):
#         self.__privateV1=" hehehehe"
#         self.__privateV2=123
#         self.__privateV3=34.44
#         print("hello")
#         self.__privateV4=True
#     def __privateF(self):
#         print(self.__privateV1)
# obj1= Myclass()
# obj1._Myclass__privateF() # here is the reason why we have the access of private variable bcoz of nothing is truly private in python \


# reference variable 
# class Xyz:
#     def __init__(self,name ):
#         self.name=name
#     def Phello(self):
#         print("hello",self.name)
# def myF(nu):
#     print("hello",nu)
# obj=Xyz("shubham") # obj is a reference variable here 
# myF(obj.name)
# obj.Phello()

# class Myclass:
#     def __init__(self,n1,n2,n3):
#         self.__privateV1=n1
#         self.__privateV2=n2
#         self.__privateV3=n3
#     def pData(self):
#         print("name 1st:{} name 2nd:{} name 3rd:{}".format(self.__privateV1,self.__privateV2,self.__privateV3))
# obj1=Myclass("shubham","khushi","arpan")
# obj2=Myclass("yoo","nft","cypto")
# obj3=Myclass("hhheeee","hehehehe","hihihihih")
# l1=[obj1,obj2,obj3]
# l2=[]
# for i in l1: 
    # i.pData() # it will print all the data of every object
    #  l2.append(i._Myclass__privateV1) # it will createb an a new list which store all the objects privateV1 variables daata in side a new list
# print(l2)
# class Xyz:
#     glo_vari="hello shubham"
#     def __init__(self):
#         self.__greet="namaste"

#     def pAll(self):
#         print(self.__greet," ",Xyz.glo_vari)
#         Xyz.glo_vari=3
#         print(Xyz.glo_vari)
# obj=Xyz()
# obj.pAll()

# static variable example 
# Write a class that counts how many objects have been created using a class variable
# class Myclass:
#     counter=0
#     def __init__(self):
#         Myclass.counter +=1
#         print("object create !")
# ob1=Myclass()
# ob2=Myclass()
# ob3=Myclass()
# ob4=Myclass()
# ob5=Myclass()
# print(Myclass.counter)


