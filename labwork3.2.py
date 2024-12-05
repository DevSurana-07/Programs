#(Q1)
'''
s1 = {12,13,14,90,45,12,13,16,14,20}
s1.add(50)
s1.remove(20)
print(s1)
print(type(s1))
print("A set is a data structure designed to hold unique elements.Its behavior is rooted in the mathematical concept of a set,which defines a collection of distinct objects. Here’s why sets do not allow duplicates:")

#(Q2)
dict1 = {'Name':'Alice','age':25,'city':'New York'}
dict1['country'] = 'USA'  # ADD
print(dict1)
dict1['Name'] = 'Dev'
print(dict1) #CHANGING THE EXISTING ONE
del dict1['age']   #DELETING THE KEY VALUE
print(dict1)


#(Q3)
list1=[]
s1 = int(input("ENTER THE NUMBERS :-- "))
for i in range(s1):
    s2 = int(input("ENTER THE VALUES:-- "))
    list1.append(s2)
s3=set(list1)
s4=list(s3)
print(s4)


#(Q4)
product={}
a1 = int(input("ENTER THE NUMBERS :-- "))
for i in range(a1):
    product_name = input("Enter the product name:-- ")
    product_price = float(input("Enter the product price :-- "))
    product[product_name]=product_price
highest_price=max(product.values())

for name in product:
    if product[name] == highest_price:
        highest_product = name
print(f"\nThe product with the highest price is {highest_product}, {highest_price}")

'''

    
    

    
    
