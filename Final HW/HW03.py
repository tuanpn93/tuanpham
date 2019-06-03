import numpy as np

myList = np.random.uniform(low=-10, high=10, size=(80,))

x = np.array(myList).reshape(10, 8)

print(x)

n = input("Enter a float number: ")
num = float(n)
print("Num : ", n)

closest = x[(0, 0)]
min = abs(num - closest)
print("First Min : ", min)

for cell in x.flatten():
    if abs(cell - num) < min:
        min = abs(cell - num)
        closest = cell
    print("Closest: ", closest)

print("Final closest : ", closest)