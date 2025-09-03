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
se={1,"hello",'a',(1,2)}
print(type(se))