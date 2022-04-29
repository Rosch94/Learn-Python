#Guide I´m using: https://www.learnpython.org/
# 
# print("This line will be printed.")
#

#Indentation instead of Braces are used standard is 4 spaces
#x = 1
#if x == 1:
#    # indented four spaces
#    print("x is 1.")
#

#
#Skip the first parts since im learing only noob stuff.
#
#Do The First Exercise
# 
#easy only assignment
# change this code
#mystring = "hello"
#myfloat = 10.0
#myint = 20

# testing code
#if mystring == "hello": # : is used for string comparison
#    print("String: %s" % mystring) 
#if isinstance(myfloat, float) and myfloat == 10.0: #type comparison and valu comparison is needed here
#    print("Float: %f" % myfloat)
#if isinstance(myint, int) and myint == 20: #type comparison and valu comparison is needed here
#    print("Integer: %d" % myint)

#mylist = [] #list assignment 
#mylist.append(1)
#mylist.append(2)
#mylist.append(3)
#print(mylist[0]) # prints 1
#print(mylist[1]) # prints 2
#print(mylist[2]) # prints 3

# prints out 1,2,3
#for x in mylist: #for iteration we use: at the end of the list
#   print(x) # it is iterrating 2 times because the position cout begins at 0



#Exercise 2 

numbers = []
strings = []
names = ["John", "Eric", "Jessica"]


#my solution was wrong //numbers.append(1,2,3)
numbers.append(1)
numbers.append(2)
numbers.append(3)
#my solution was wrong //strings.append("numbers", "hello")
strings.append("hello")
strings.append("world")

# write your code here
second_name = names[2]

# this code should write out the filled arrays and the second name in the names list (Eric).
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)