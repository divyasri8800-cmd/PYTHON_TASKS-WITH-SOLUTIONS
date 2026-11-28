#file handling

#read

f= open(r"C:\Users\divya\OneDrive\Desktop\demo.txt.txt","r")
print(f.read())

f= open(r"C:\Users\divya\OneDrive\Desktop\demo.txt.txt","r")
print(f.readlines())

f= open(r"C:\Users\divya\OneDrive\Desktop\demo.txt.txt","r")
print(f.readline())


#write

f=open(r"C:\Users\divya\OneDrive\Desktop\demo.txt.txt","w")
f.write("wlcome to livewire")

f=open(r"C:\Users\divya\OneDrive\Desktop\demo.txt.txt","r")
print(f.read())
f.close()


#append
f=open(r"C:\Users\divya\OneDrive\Desktop\demo.txt.txt","a")
f.write("no act of kindness")
f=open(r"C:\Users\divya\OneDrive\Desktop\demo.txt.txt","r")
print(f.read())


#create a new file

f1=open(r"C:\Users\divya\OneDrive\Desktop\divya.txt.txt","a")
f1.write("All is well")
f1=open(r"C:\Users\divya\OneDrive\Desktop\divya.txt.txt","r")
print(f1.readlines())
f1.close()


#exception +file handling

try:
    file=open(r"C:\Users\divya\OneDrive\Desktop\divya.txt.txt","r")
    print(file.read())
    file.close()
except NotFoundError:
    print("File does not exist")

#text
#read
with open(r"C:\Users\divya\OneDrive\Desktop\demo.txt.txt","r+") as file:
    print(file.read())

#write
with open(r"C:\Users\divya\OneDrive\Desktop\demo.txt.txt","w+") as file:
    file.write("Hello python")

with open(r"C:\Users\divya\OneDrive\Desktop\demo.txt.txt","r+") as file:
    print(file.read())

#append
with open(r"C:\Users\divya\OneDrive\Desktop\demo.txt.txt","a+") as file:
    file.write(" Welcome")
    

with open(r"C:\Users\divya\OneDrive\Desktop\demo.txt.txt","r+") as file:
    print(file.read())

#binary
#rb
with open(r"C:\Users\divya\OneDrive\Desktop\demo.txt.txt","rb") as file:
    print(file.read())

#wb
with open(r"C:\Users\divya\OneDrive\Desktop\demo.txt.txt","wb") as file:
    file.write(b"Hello python")

with open(r"C:\Users\divya\OneDrive\Desktop\demo.txt.txt","rb") as file:
    print(file.read())
    
#append
with open(r"C:\Users\divya\OneDrive\Desktop\demo.txt.txt","ab") as file:
    file.write(b" Welcome")

with open(r"C:\Users\divya\OneDrive\Desktop\demo.txt.txt","rb") as file:
    print(file.read())

#rb+

with open(r"C:\Users\divya\OneDrive\Desktop\demo.txt.txt","rb+") as file:
    print(file.read())
    file.write(b"hello")

#wb+
with open(r"C:\Users\divya\OneDrive\Desktop\demo.txt.txt","wb+") as file:
    file.write(b"hai Divya")
    file.seek(0)
    print(file.read())

#ab+

with open(r"C:\Users\divya\OneDrive\Desktop\demo.txt.txt","ab+") as file:
    file.write(b" and bhavya")
    file.seek(0)
    print(file.read())


#example1

name= input("Enter Student Name:")
with open(r"C:\Users\divya\OneDrive\Desktop\student.txt.txt","a") as f:
    f.write(name)
print("Student saved successfully")


#example2

amount=input("Enter a amount:")
with open(r"C:\Users\divya\OneDrive\Desktop\student.txt.txt","a") as f:
    f.write("5000" +amount)
print("Transaction saved")

with open(r"C:\Users\divya\OneDrive\Desktop\student.txt.txt","r") as f:
    print(f.read())



 


























































    



































