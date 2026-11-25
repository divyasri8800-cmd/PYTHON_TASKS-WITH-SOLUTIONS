#tuple

#1

t=(10,20,"Divya", True)
print(t)



#3
tup=(10,100,1000)
a,b,c = tup
print(a)
print(b)
print(c)

#4
a=(11,22,33,44,55)
b=list(a)
b.append(66)
a=tuple(b)
print(a)

#5
x=(5,10,15,20,25)
print(x.index(10))

#6
y=(36,42,48,54,60)
print(len(y))

#7
z=(10,20,30,40,50,60)
t=z[::-1]
print(t)

#8

x=(12,24,36,48,24,36)




#9
p=(7,14)
q=1
for i in p:
    q=q*i
print(q)
    
#10
tup=(1,2,3,4,5,6,7,8,9,10)
z=list(tup)
s=[]
for i in z:
    if i*i:
        s.append(i)
print(s)













