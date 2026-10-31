#list task

#1.
a=[25, 45, 36, 47, 69, 48, 68, 78, 14, 36]
a.sort()
print(a)

#2.
print(sum(a))

#3.
print(max(a))

#4.
b=[25, 45, 36, 47, 69, 47,48, 68, 78, 14, 36]
b1=set(b)
print(b1)
b3=list(b1)
print(b3)

#5.
c=b.copy()
print(c)

#6.
colour=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
colour.remove('Red')
colour.remove('Pink')
colour.remove('Yellow')
print(colour)

#7.
num=[20,35,70,44,50,13,17,3,5]
l=[]

for i in num:
    if i%2==1:
        l.append(i)

print(l)


#8.
print(num.index(44))

#9.
a.extend(b)
print(a)

#10.
x=[22,33,44,55]
y=[33,44,55,66]
x1=set(x)
y1=set(y)
z=x1.intersection(y1)
print(z)
s=list(z)
print(s)

#11.
m=[10,20,30]
n=[20,30,40]

l=[20,30]
m1=[10,20,30,20,30,40]
m2=[]
for i in m1:
    if i not in l:
        m2.append(i)
print(m2)

#12.
a1=[67,83,12,44,99]
a2=[55,16,30,13,6]
a1.extend(a2)
print(a1)
ecount=0
ocount=0
for i in a1:
    if i%2==0:
        ecount+=1
    else:
        ocount+=1
print(ecount)
print(ocount)


#13.

num1=[32,-10,16,20,-11]

neg=[]
pos=[]

for i in num1:
    if  i<0:
        neg.append(i)
    else:
        pos.append(i)
print(neg)
print(pos)








































