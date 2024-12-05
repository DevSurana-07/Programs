#(Q1)

first_name = str(input("Enter your name :-- "))
last_name = str(input("Enter your name :-- "))
print(f"Helllo {last_name} {first_name}!")

#(Q2)

item=str(input("Enter the item name  :-- "))
price = float(input("Enter the price :-- "))
print(f"The price of {item} is {price} dollars.")


#(Q3)

name = "level"
a = name[0:5]
b = name[::-1]
print(a,"The word is palindrome")
print(b,"The word is palindrome")



#(Q4)

user1= str(input("Enter your name :-- "))
print(user1.upper())
print(user1.lower())
print(user1.title())


#(Q5)

user2 = [1,2,3,4,5,6,7,8,9,10]
user2.append(11)
print(user2)



#(Q6)

user_input = input("Enter the items for the list, separated by commas: ")
user_list = user_input.split(",")
user_list = [item.strip() for item in user_list]
print("Your list is:", user_list)
print("The minimum number in the list is :--  ",min(user_list))
print("The maximum number in the list is :--  ",max(user_list))



#(Q7)

my_tuple = (1, 2, 2, 3, 4, 4, 5)
unique_values = set(my_tuple)
print("Unique values:", unique_values)




#(Q8)

list1=[1,2,3,4,5]
list1[3]=5
print(list1)



#(Q9)

list2=[1,2,3,[4,5,6],7,8]
list2[4]=9
print(list2)

#(Q10)
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
nested_list[1][1] = 99 
print(nested_list)

#ADD
nested_list[0].append(10)
print(nested_list) 

#REMOVE
nested_list[2].remove(9)
print(nested_list)

#REPLACE
nested_list[1] = [100, 200, 300]  
print(nested_list)  



#(11)
summ =(([1,2],[3,4],[5,6]))
summ[0][1]=99
print(summ)


#(Q12)

a = 10
b = 20
# Swap using a temporary variable
temp = a
a = b
b = temp
print("a =",a)
print("b =",b)


#(Q13)
a = 5
b = 10

a = a + b  
b = a - b  
a = a - b  

print("a =", a, "b =", b)














































































































































