#1.Write a Python program to insert items into a list in sorted order
#Expected Output:
#Original List:
#[25, 45, 36, 47, 69, 48, 68, 78, 14, 36]
#Sorted List:
#[14, 25, 36, 36, 45, 47, 48, 68, 69, 78]
'''
a=[25, 45, 36, 47, 69, 48, 68, 78, 14, 36]
print("Original List:")
print(a)

a.sort()
print("Sorted List:")
print(a)
'''

#2. Write a Python program to sum all the items in a list.
'''
n=[10,20,30,40]
total=0
for i in n:
    total=total+i
print("Sum:", total)
'''
#3.Write a Python program to get the largest number from a list.
'''
num=[20,40,60,80,100]

largest=0
for i in  num:
    if i > largest:
        largest=i
print("Largest number:", largest)
'''
#4. Write a Python program to remove duplicates from a list.
'''
a=[11,22,33,33,44,44,55]
b=[]
for i in a:
    if i not in b:
        b.append(i)
print(b)
'''
#5.Write a Python program to clone or copy a list.
'''
m=[110,120,130,140,150]
a=m.copy()
print("Copied list:", a)
'''
#6.6.Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
'''
l1= ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
del l1[5]
del l1[4]
del l1[0]
print(l1)
'''
#7.Write a Python program to print the numbers of a specified list after removing even numbers from it.
'''
a=[1,2,3,4,5,6,7,8,9,10]
b=[]
for i in a:
    if i%2==1:
        b.append(i)
print(b)
'''

#8.Write a Python program to access the index of a list.
'''
a=[11,12,13,14,15,16,17,18,19,20]
print(a.index(16))
'''

#9.Write a Python program to append a list to the second list.
'''
num=[99,88,77,66]
num.append(55)
print(num)
'''
#10.   Find common elements between two lists.
'''
a=[22,32,42,52,62]
b=[2,12,22,32,72,82]

for i in a:
    if i in b:
        print(i)
'''
#11.   Find elements present in one list but not in another.
'''
a=[22,32,42,52,62]
b=[2,12,22,32,72,82]

for i in a:
    if i not in b:
        print(i)
'''






















