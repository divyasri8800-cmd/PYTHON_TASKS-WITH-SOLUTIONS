'''#1) Reverse a string.
#method1
a = " Divyasri"
##print(a[::-1])
#method2
b="".join(reversed(a))
print(b)

#2) Check whether a string is palindrome
text= "level"
if text == text[::-1]:
    print("palindrome")
else:
    print("not palindrome")

#3)Count number of vowels in a string.
name = "Divyasri"
count= 0
for i in name:
    if i in "aeiou":
       count +=1
print(count)
    
#4) Count number of consonants in a string.
name = "Divyasri"
count= 0
for i in name:
    if not i in "aeiou":
       count +=1
print(count)

#5) Count total characters in a string (without using length()).
place= "mettur dam"
count = 0
for i in place:
    count += 1
print(count)

#6)Convert string to uppercase without using toUpperCase().
text = "hello"
result = ""
for x in text:
    if x == "h":
        result += "H"
    elif x == "e":
        result += "E"
    elif x == "l":
        result += "L"
    elif x == "o":
        result += "O"
print(result)


#7)  Convert string to uppercase without using toUpperCase().
text = "HELLOW"
result = ""
for x in text:
    if x == "H":
        result += "h"
    elif x == "E":
        result += "e"
    elif x == "L":
        result += "l"
    elif x == "O":
        result += "o"
print(result)

#8)  Remove spaces from a string.
name="Divya Sri"
result=""
for i in name:
    if i != " ":
        result += i
print(result)

#9) Count number of words in a string.
m= "I like python too "
count=0
for i in m.split():

    count+=1

print("Count number of words: ",count)
    
#10)Find first occurrence of a character

x=input("Enter a name:")
ch=input("Enter a character:")

for i in range(len(x)):
    if x[i]==ch:
        print(i)
        break

#12. Replace all spaces with hyphen (-).

x=input("Enter a string:")
print(x.replace(" ","_"))

#13. Check whether string contains only digits.
                
num=input("Enter a num:")
print(num.isdigit())

#14. Compare two strings without using equals().

m=input("Enter a first string:")
n=input("Enter a second string:")

if m==n:
    print("Equal")
else:
    ("Not equal")

#15. Concatenate two strings without using + operator.

m=input("Enter a first string:")
n=input("Enter a second string:")

print(" ".join([m,n]))


#17. Find frequency of each character

name=input("Enter a name:")
for i in name:
    print(i,name.count(i))

#18. Find largest word in a sentence.

a = input("Enter a sentence:")
word=a.split()
largest=max(word, key=len)
print("Largest word:", largest)

'''
#19. Count uppercase, lowercase, digits, special characters
'''
n=input("Enter a password:")
upper=lower=digit=special=0
for i in n:
    if i.isupper():
        upper +=1
    elif  i.islower():
        lower +=1
    elif i.isdigit():
        digit +=1
    else:
        special +=1

print("Uppercase:", upper)
print("Lowercase:", lower)
print("Digits:", digit)
print("Special character:" ,special)

'''
#20.  Reverse each word in a sentence
'''
s=input("enter a sentence:")

word=s.split()

for i in word:
    print(i[::-1],end=" ")

'''
#21. Check whether two strings are anagrams.
'''
s1=input("Enter a character:")
s2=input("Enter a character:")

count = 0
for ch in s1:
    if ch in s2:
        count=count+1
if count == len(s1):
    print("Anagram")
else:
    print("Not anagram")

'''
#22. Remove a specific character from string.
'''

a=input("name of a fruit:")
ch=input("Enter a remove character:")
a=a.replace(ch,"")
print(a)
'''

#23. Find second most frequent character.
'''
n=input("Enter a string:")
count=0
for i in n:
    
    for j in n:
        if i==j:
            count=count+1
    print(i,count)
'''

#24.Print all substrings of a string.
'''
n=input("Enter a string:")

for i in range(len(n)):
    for j in range(i+1,len(n)+1):
        print(n[i:j])
'''
#25.  Find longest substring without repeating characters.
'''
m=input("Enter a string:")

result =""
for ch in m:
    if ch not in result:
        result=result+ch
print("Longest substring:", result)
'''

#27. Find first non-repeating character
'''
s= input("Enter a string:")

for i in s:
    if s.count(i)==1:
        print(i)
        break
'''












