#1
x={10,20,40,80}
x.remove(40)
print(x)

#2
x.discard(20)
print(x)

#3
a={44,74,46,83}
b={55,90,45,76,44}
a.difference(b)
print(a)

#4
y={83,10,15,18}

y.clear()
print(y)


#5
a1=list(a)
print(max(a1))
print(min(a1))

#6
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))

#7
print(a.isdisjoint(b))

#8
a1=list(a)
c=[]
for i in a1:
    if i%2==0:
        c.append(i)
print(c)
s=set(c)
print(s)

#9
a2={44,74,46,83}
b2={55,90,45,76,44}
print(a2.symmetric_difference(b2))

        















