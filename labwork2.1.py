
# (Q1)

a = int(input("enter the number :--   "))
if a%2==0:
    print("The number is even ")
else:
    print("The number is odd ")



# (Q2)

age = int(input("enter the age :--  "))
if age <60 :
    if  age <=12:
        print("'you are adult")
    elif age <=19:
        print("you are a teenager")
else:
    print("you are a senior")
    

    


#(Q3)

a1 = int(input("enter the number "))
b =int(input("enter the number "))
c = int(input("enter the number "))

if a1>b:
    if a1>c:
        print("a1 is max")
    else :
        print("c is max ")
else:
    if b>c:
        print("b is max")
    else:
        print("c is max ")

#(Q4)
user_1 = int(input("Enter the number :---  "))
user_2 = int(input("Enter the number :---  "))
operations = input("Enter the operation (+, -, *, /): ")
if operations == '+' :
    result = user_1 + user_2
    print("the sum is :--   ",result)
elif operations == '-' :
    result = user_1 - user_2
    print("The sub is :-- " ,result)
elif operations == '*' :
    result = user_1 * user_2
    print("The multipication  is :-- " ,result)
elif operation == '/':
    if num2 != 0:  
        result = num1 / num2
        print("The result of division is:--   ",result)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation. Please enter +, -, *, or /.")
    
#(Q5)

i = int(input("enter the number :-- "))
while i <= 10:
    print(i)
    i += 1


#(Q6)
#1.

for i in range (1,11,1):
    print(i)

#2.

for i in range (1,11,1):
    print(i**2)

#(Q7)

i = 1
while i <= 50:
    if  i%2 == 0:
        print(i)
    i = i + 1


#(Q8)

#1.
for i in range (1,21,1):
    print(i)

    
#2.

for i in range (1,21,1):
    if i%2 == 1:
        print(i)


#(Q9)

for i in range (5,51,5):
    print(i)



#(Q10)

for i in range (10,0,-1):
    print(i)


#(Q11)


for i in range(1,51):
    if i%2 == 0 and  i%3 == 0:
        print(i,":-Both are divisible by 2 and 3")
    elif i%2 == 0 and i%3 != 0:
        print(i,":-The number is divisible by 2")
    elif i%2 != 0 and i%3 == 0:
        print(i,":-The number is divisible by 2")
    else:
        print(i)
































    


