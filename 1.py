'''
import pandas as pd
import matplotlib.pyplot as plt

x = [25,26,27,28,29]
y = [10,20,30,40,50]
plt.plot(x,y)
plt.show()


i = 1
while i<=10:
    if i == 7:
        break
    print(i)
    i = i+1


bst=[i**2 for i in range(1,11)]
print(bst)

for i in range (1,6):
    for j in range (5,i-1,-1):
        print("*",end = '',sep = "  ")
    print()

for i in range (1,6):
    for j in range (1,i+1):
        print(chr(64 + i),end="",sep="")
    print()

print("Step 1")
print("Step 2")
print("Step 3")

for i in range(1,21):
    if i%2 == 0:
        print(i)

a = {12,13,14,15,16,25,88,99,24,51,62,12}
b = {55,56,57,58,59,60,51}
a.add(100)
print(a)
a.remove(99)
print(a)
set1 = a.union(b)
print(set1)
set1 = a.intersection(b)
print(set1)
'''
def calculate_area(length, width):
    """
    Calculate the area of a rectangle.

    This function takes two arguments:
    - length: The length of the rectangle.
    - width: The width of the rectangle.

    Returns:
    - The area of the rectangle (length * width).
    """
    return length * width

# Accessing the docstring
print(calculate_area.__doc__)

# Example usage of the function
area = calculate_area(10, 5)
print(f"The area of the rectangle is: {area}")





































































