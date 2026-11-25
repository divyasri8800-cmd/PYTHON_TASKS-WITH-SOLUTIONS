#1
dict={1:10,2:20,3:30}
dict[4]=40
print(dict)

#2

#3
x={'A':1,'B':2,'C':3}
for i in x:
    print(i,x[i])

#4
a={}
for i in range(1,16):
    if i<=15:
        a[i]=i*i
print(a)

#5
a1={'Name':'Divya','Age':'21'}
a2={'Course':'Python','place':'salem'}
a3=a1|a2
print(a3)

#6
price={1:100,2:200,3:300}
l=list(price.values())
print(sum(l))

#7
p=['a','b','c']
q=[10,20,30]


r={}

for i in range(len(p)):
    if i< len(q):
        r[p[i]]=q[i]
print(r)

#8

        





















