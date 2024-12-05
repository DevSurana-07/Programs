#LAB WORK
# 1.3

#(Q1).


a = int(input("ENTER THE NUMBERS :-   "))
a1 = float(a)
a2 = bool(a)
print("THE NUMBER IS IN INTEGER :-  ",a)
print("THE NUMBER IS FLOAT :-  ",a1)
print("THE NUMBER IS BOOLEAN:-  ",a2)

#(Q2)


b = 20.22
b1 = int(b)
print("THE NUMBER IS FLOAT :-  ",b)
print("THE NUMBER IS CONVERTED INTO FLOAT :--",b1)
print("ABOVE NUMBER HAS BEEN CONVERTED INTO INTEGER WITH THE HELP OF INT FUNCTION")


#(Q3)


c = bool(input("ENTER THE VALUE:--  "))
c1 = int(c)
c2 = str(c)
print("the value is :--  ",c)
print("the value is :--  ",c1)
print("the value is :--  ",c2)


#(Q4)

d = 22
e = 66.25
f = "hello"
g = True
h = [1,2,3]
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))
print("THE ID IS :-- ",id(d))
print("THE ID IS :-- ",id(e))
print("THE ID IS :-- ",id(f))
print("THE ID IS :-- ",id(g))
print("THE ID IS :-- ",id(h))

print("the type and id of variable are shown above")




#(Q5)

a=5
b=5
print(id(a))
print(id(b))
# YES THE MEMORY ADDRESS ARE SAME IN THE ABOVE CASE.
print("---------------------------------------------------------------------------------------------------------------")
# THE VARIABLE IS CHANGED
A =5
B= 6
print(id(A))
print(id(B))

# THE MEMORY ADDRESS IS DIFFERENT IN THE ABOVE CASE.
