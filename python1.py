# a = [[n*5, n*5*2] for n in range(1,4)]
# print(a)

# a = 'hello world'
# print(a[6:-3])

# str = "hello world"
# newStr = str.replace('hello', 'bye')
# print(newStr)

#Lay pphan tu cuoi mang
# numbers = [1,2,3]
# a = numbers.pop()
# print(a)

# print(numbers)
# #index() tra ve vi tri cua phan tu else Exception
# #list.reverse() Dao nguoc thu tu cac phan tu trong mang
# numbers.reverse()
# print(numbers)

# nb = [3,45,5,3,5,2,44,65]
# nb.sort()
# print(nb)

#Tuple khai bao = (...) va khong thay doi duoc gia tri

#Dictionary khai bao = {...}
# point = {'x':1,'y':2}
# print(point['x'])
#Them 1 phan tu dict[key] = value Them pt vao dau Oj
# #dict.clear() xoa toan bo
# aa = {'s','d','f','g'}
# print (aa)
# value = 5
# a = dict.fromkeys(aa,value)
# print(a)
# # Tao 1 dict tu cac pt trong list -> gan gia tri = value

# #dict.has_key(key): Kiem tra 1 key co ton tai trong Oj?
# print(dict.has_key('s'))

# dict = {'Ten': 'Hoang', 'Tuoi': 20}

# print ("Gia tri : %s" %  dict.has_key('Tuoi'))
# print ("Gia tri : %s" %  dict.has_key('Gioitinh')) 
# AttributeError: 'dict' object has no attribute 'has_key'
#has_key bbi loai bo thay = in

# aa = {'s','d','f','g'}
# dictional = dict.fromkeys(aa,5)
# print(dictional)
# che = dictional.keys()
# vlu = dictional.values()
# print(che)
# print(vlu)

#Phan chia module/Thu vien
# 3 loai module thuong thay .py,
# thu vien: .dll, .pyd, .so, .sl ....
# C-module lien ket voi trinh phien dich

#Time
# import time
# import calendar

# print(time.localtime())
# print(time.time())
# print(time.asctime(time.localtime()))

# cal = calendar.month(2020,12)
# print(cal)
# # print(time.clock())
# print(calendar.monthrange(2020,12))

# def fib(n):
#     result = []
#     a,b = 0,1
#     while b<n:
#         result.append(b)
#         a, b = b , a + b
#     return result
# f = fib(100)
# print(f)
# -- mypack
#     --python1.py
#     --FirtCode.py
# import math

# def Cong(a,b):
    
#     return globals()

# def Tru(a, b):
#     return a - b

# print(Cong(2,3))    

#Class

# class SieuNhan:
#     sucmanh = 50
#     def __init__(self, para_ten, para_vukhi, para_mausac):
#         self.ten = para_ten
#         self.mau = para_mausac
#         self.vukhi = para_vukhi

# class SieuNhanGao(SieuNhan):
#     def __init__(seft, para_ten, para_vukhi, para_mausac, para_sieuthu):
#         super().__init__(para_ten, para_vukhi, para_mausac)
#         seft.sieuthu = para_sieuthu

# GaoDo = SieuNhanGao('Bac','Kiem','Trang-Xam','Soi')
# print(GaoDo.__dict__)
# print(GaoDo.sucmanh)

#Thao tac file va foder
# import os
# fh = open('text.txt', 'r')
# print(fh)
# data = fh.read()
# print(data)
# fh.close()
# os.remove('text.txt')
#os.mkdir('text')
#os.rmdir('text')

import json
# listfruits = '{"orange" : "Qua cam", "strawberry": "Dau tay",'\
#     '"grape": "Nho", "durian":"Sau rieng"}'
# mylist = json.loads(listfruits)

# print(mylist)
# print(mylist['durian'])

# #Khai bao  JSON string
# coffees = {"Capuchino":"Cafe Italian", "Expresso":["Matcha","Mocha"], "VietNam":True, "Latte": 32 }

# #ghi du lieu vao file coffee.txt
# with  open('coffee.txt', 'w') as myfile:
#     json.dump(coffees, myfile)

# print("success")    

#KB
# listTraiCay = {
#     "mango":"Qua xoai",
#     "straxberry":"Dau tay",
#     "avocado": "Qua bo",
#     "durian":"Qua sau rieng",
#     "orange": "Qua cam",
#     "lemon": "Qua chanh",
#     "coconut":"Qua dua"
# }

# #Xu li va sap xep ket qua Json theo key
# print(json.dumps(listTraiCay, indent=4, sort_keys=True))

import json
x = {
    "name":"ken",
    "age":45,
    "married":True,
    "children": ("Alice", "Bob"),
    "pet": ["Dog"],
    "car": [
        {"model": "Audi A1", "mpg":15.1},
        {"model": "Zeep","mpg": 18.1}
    ],
}

sorted_String = json.dumps(x, indent=4, sort_keys=True)
print(sorted_String)