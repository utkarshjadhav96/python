# # # a = """ownovnn
# # # vjnjnve
# # # vjneenve
# # # jnvjenve
# # # vnjenve"""

# # # print(a)

# # # print("own" in a)

# # # b = "Hello world"
# # # print(b[-3:-2])

# # # c= "   utkarsh   jadhav   "
# # # print(c.strip())

# # # c = "utkarsh, jadhav , wemotive, baner"

# # # print(c.split(","))

# # age = 36
# # age =35
# # txt = f"My name is wemotive, I am {age:.4f}"
# # print(txt)

# # xt = f"total is  dollors"
# # print(xt)

# # xt = "Sara is out Project or product"
# # # print(xt)
# # # print(xt.find("a"))
# # # print(xt.index("a"))
# # # print(xt.format())
# # age =24
# # a = "age is {age}".format(age = 23)
# # print("wemotive".title())

# # class myclass():
# #     def __len__(self):
# #         return 0
# #     def myfunction():
# #         return 0
    
# # myobj = myclass()

# # print(bool(myobj.myfunction))

# def lisst(list1, list2):
#     # list1 =["wemotive", "Abhinandan", "Khushi", "Akash"]
#     # print(list1)
#     # # list1.append("Utkarsh")
#     # print(list2)
#     # list1.extend(list2)
#     # print(list1)
#     # # list1[1:1]=["Akshay","wemotive", "Abhinandan"]
#     # # list1.insert(2,"Forge")
#     # list1.remove("Utkarsh".lower())
#     # del list1[3]
#     # list1.clear()
#     # print(list1)

#     list1.extend(list2)
#     # for i in list1:
#     #     print(i)

#     # for i in range(len(list1)):
#     #     print(list1[i])
#     # i= 0
#     # while i < len(list1):
#     #     print(list1[i])
#     #     i += 1
    
#     [print(x) for x in list1]

# # lisst([1,2,4,1,2], [3,4,"utkarsh"])
# class function:
#     def func(self, list):
#         li = []
#         for i in list:
#             if 'a' in  i:
#                 li.append(i)

#         return li
#     def sorting(self, list):
#         list.sort()
#         return list
    
#     def descending(self,list):
#         list.sort(reverse = True)

#         return list

# l1 = function()
# print(l1.func(["dgv","ertgqa", "rtagv", "agvdf","2tgv"]))

# print(l1.sorting([2,5,23,23,34,-43,233,5,5426,4]))
# print(l1.sorting(["utn",'e','ewvww','wew',"22","4","2"]))

# thislist = l1.descending(["orange", "mango", "kiwi", "pineapple", "banana"])
# print(l1.descending(["utn",'e','ewvww','wew',"22","4","2"]))

# print(thislist)

# l = ["utn",'e','ewvww','wew',"22","4","2"]
# l.sort(reverse = 0)
# print(l)

# l.reverse()
# print(l)
# t1 = (1,3,5,3,2)
# class myClass:
#     def insert_tuple(self, s):
#         global t1
#         t = list(t1)
#         t.insert(0,s)
#         t.append(s)
#         t1 = tuple(t)
#         print(t1)
#         del t1

# o1 = myClass()
# print(t1)
# o1.insert_tuple(100)

# s1 =  {"apple", "banana", "cherry"}
# s2 = {"ve","vrv", "3r3"}

# print(s1)

# s1.update(s2)

# print(s1)

# s1.remove("ve")
# print(s1)
# # s1.remove("as")
# # print(s1)
# s1.discard("3r3")
# print(s1)

# s2.clear()
# print(s2)

# del s1

# s = "    wemotive is a best      company .  It    is located   in  baner"
# print(s)
# s = " ".join(s.split())
# print(s)

# class myNum:
#     def __iter__(self):
#         self.a = 1
#         return self

#     def __next__(self):
#         if self.a <= 5:
#             x = self.a
#             self.a += 1
#             return x
#         else :
#             raise StopIteration
    

# myclass = myNum()
# myiter = iter(myclass)

# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))

# 
# import datetime
# x = datetime.datetime.now()

# print(x.year)
# print(x.month)
# # print(x.date)
# print(x.day)
# print(x.strftime("%A"))


# y = datetime.datetime(2025, 5 ,15)
# print(y)

# import math

# x = min(34,53,32,1,1,-144)
# print(x)

# y = max(2432,53235,141,53,2353)
# print(y)

# x = abs(x)
# print(x)

# z= pow(3,5)
# print(z)

# print(math.sqrt(65))
# print(math.ceil(-1.4))
# print(math.floor(1.4))
# print(math.pi)

# import re

# txt = "The rain in spain"
# x = re.findall("Portugal", txt)
# print(x)


# def myfun(country = "India"):
#     print("I am From ", country)

# myfun("Japan")
# myfun("China")
# myfun()

# def my_function(animal, name):
#   print("I have a", animal)
#   print("My", animal + "'s name is", name)

# my_function(animal = "dog", name = "Buddy")

# def myfun(*kids):
#     print("Child name is" ,kids[1])

# myfun("Emil","Wemotive", "Utkarsh")


# def myfun(name ,**myvar):
#     print("Type:" ,type(myvar))
#     print("Name :" ,name)
#     print("Age :", myvar["age"])
#     print("all data :" , myvar)

# myfun(name = "Tobias", age = 30, city = "Pune")

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# p1 = Person("Utkarsh", 22)

# print(p1.name)
# print(p1.age)

# class Person:
#     def __init__(self,name,last):
#         self.fname = name
#         self.lname = last

#     def printname(self):
#         print(self.fname, self.lname)

# class student(Person):
#     def __init__(self,name, last, year = 2020):
#         super().__init__(name, last)
#         self.year = year

#     def welcome(self):
#         print("Year :" ,self.year)

# x = student("utkarsh", "Jadhav")
# x.printname()
# x.welcome()

# f = open("guess_num.py")
# print(f.readlines())
# f.close()

# with open("main.py") as y:
#     print(y.read(5))

# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#     return wrapper

# @my_decorator
# def say_hello():
#     print("Hello!")

# say_hello()

# l = {x for x in "banana"}
# print(l)

# a = [x**2 for x in range(5)]
# print(a)

# b = {s:s**3 for s in range(5)}
# print(b)

# x = 10

# def fxn():
#     global x
#     x = 22
#     print(x)

# fxn()
# print(x)
import sys

def clean_data(data):
    return data.strip().lower()

def main():
    """Main entry point for the application logic."""
    if len(sys.argv) > 1:
        raw_input = sys.argv[1]
        print(f"Cleaned output: {clean_data(raw_input)}")
    else:
        print("Usage: python data_processor.py <text_to_clean>")

if __name__ == "__main__":
    main()