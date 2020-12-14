# print ('hello')

# a = 1
# b = 'hello world \t \n'
# c = [1,2,3]
# d = [1.2, 'hello']
# print(a)
# print((b + "    ") * 3 )
# print(len(b))

# point = 2 ,3 
# print (point)
# # print (point[0])

# # yellow = ( 2 , 3,6)
# # a,b,c = yellow
# # print(a,b,c)

# # Nam = {
# #     'name':"Phuc",
# #     'age':'23',
# #     'email':"fireman@..."
# # }

# # print (Nam)

# # print (Nam['name'], Nam['age'], Nam['email'])

# x = {1,2,3,1,2}

# print(x)

# x = 'awesome'

# def myFunc():
#     x = "fantastic"
#     print("Python is " + x)

# myFunc()

# print('Python' + x)

# x = range(6)

# print (x[3])

#IF ELIF ELSE.....

# if x[1] > 4:
#     print (True)
# elif x[1] > x[0]:
#     print('hihi')    
# else:
#     print(False)

# print('This is ex1') if x[1] > x[2] else print('This is ex2')

# #Verry fun
# a = 330
# b = 330
# print("A") if a > b else print("=") if a == b else print("B")

# x = 11
# if x>10:
#     print('above ten')
#     if x>20:
#         print('and above 20')
#     else:
#         print('but not above 20')    
# else:
#     print('not above ten')

#While loop......
# i = 1
# while i<6:
#     print(i)
#     if i == 3:
#         break
#     i+=1

#Vong lap vo tan
# i = 1
# while i<6:
#     print(i)
#     # if i == 3:
#     #     continue
#     i+=1    
# else:
#     print('Else')

# i = 0;
# while i<7:
#     i += 1
#     # if i == 3:
#     #     continue
#     print(i)    

#For loop
    #For...in....
# fruits = ["Apple", "banana", "cherry"]
# for x in fruits:
#     print(x)

# for x in range(6):
#     print(x)
# #   if x == 3:
# #        break
# else:
#     print('The end')        


# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]
# for a in adj:
#     for b in fruits:
#         print(a,b)

#Function 
# def calcAge(birthYear):
#     age = 2021 - int(birthYear)
#     return age

# print(calcAge(1997))

# def funcname(*person):
#     print("persons : " + person[1])
# funcname('Tuan', 'Trung', 'Nam')


# def Function(food):
#     for i in food:
#         print(i)

# fruits = ['Cam', 'Buoi', 'Chanh']
# Function(fruits)
# x = 'x'
# def tri_recursion(k):
#   if(k > 0):
#     result = k + tri_recursion(k - 1)
#     print(result)
#   else:
#     result = 0
#   return result

# print("\n\nRecursion Example Results")
# tri_recursion(6)


# numcalls = 0
# def square(x):
#     global numcalls
#     numcalls = numcalls + 1
#     return x * x
# print(square(3))
# print(numcalls)
