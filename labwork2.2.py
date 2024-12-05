
#(Q1)

for i in range(1,21):
    if i%4 == 0:
        continue
    print(i)

#(Q2)
i = 1
while i<=10:
    if i == 7:
        break
    print(i)
    i = i +1

    
#(Q3)
string="PYTHON"
for i in string:
    if i == "A" or i == "E" or i == "I" or i == "O" or i == "U":
        continue
    print(i)


#(Q4)
lst = [i**3  for i in range (1,11) ]
print(lst)


#(Q5)

bst = [i for i in range (1,51) if i%2 == 0]
print(bst)

#(Q6)

words = ["apple", "banana", "orange", "umbrella", "grape", "elephant"]
vowels = "AEIOUaeiou"
wow = [word for word in words if word[0] in vowels]
print(wow)



#(Q7)
for i in range (1,6):
    for j in range (1,i+1):
        print("*",end = '',sep = "  ")
    print()

#CLASS WORK
    
for i in range(1,6):
    for k in range (5,i,-1):
        print("_",end="")
    for j in range(1,i+1):
        print(j,end="")
    print()

#(Q8)

for i in range (1,6):
    for j in range (5,i-1,-1):
        print("*",end = '',sep = "  ")
    print()

#(Q9)
for i in range (1,6):
    for k in range(5,i,-1):
        print('_ _',end = "")
    for j in range(1,i+1,1):
        print(i,end = "")
    print()

#(Q10)
for table in range(1, 6):  
    print("Multiplication Table for", table)
    for multiplier in range(1, 11):  
        result = table * multiplier
        print(f"{table} x {multiplier} = {result}")
    print("-" * 20)      































