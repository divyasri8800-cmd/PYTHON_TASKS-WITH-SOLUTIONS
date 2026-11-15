#exception handling

##Eg1:


try:
        a=int(input("Enter a number:"))
        b=int(input("Enter a number:"))

        r=a//b

except  ValueError:
    print(" Incorrect value")
except ZeroDivisionError as z:
    print("cannot divided by zero")
except Exception as e:
    print("errer",e)

else:
    print("Result:",r)

finally:
    print("Thank you")

    

#Eg2: raise creates or re-raises an exception
balance=int(input("Enter the amount:"))
withdraw=int(input("Enter the amount withdraw:"))

if withdraw>balance:
    raise ValueError("Invalid Balance")

balance=balance-withdraw
print("Remaining Balance:",balance)

#Eg3: assert checks whether a condition is true. If the condition is false,
##Python raises AssertionError.

age=int(input("Enter your age to vote:"))

assert age>=18,"Age must be 18 or above"

print("Eligible to vote")


#Eg4: Nested try-except

try:
    print("Outer try Started")

    try:
    
        a=int(input("Enter a first number:"))
        b=int(input("Enter a second number:"))

        res=a//b
        print("Result:",res)

    except ZeroDivisionError as z:
        print("cannot divided by zero")

except ValueError as v:
    print("Enter only the number")


#Eg5: Exception Propogation - main() handle error if subfunc fails

def calculate(x,y):
    print("Inside a calculate function")
    result = x//y
    return result

def main():
    try:
        a=int(input("Enter a first number:"))
        b=int(input("Enter a second number:"))
        calculate(a,b)

    except ZeroDivisionError as z:
        print("cannot divided by zero")

main()

#Eg6: Exception Chaining
#Connect with another exception after an exception raise

try:
    try:
        number = int("hello")

    except ValueError as e:
        raise RuntimeError("Unable to process the customer data.")from e

except RuntimeError as e:
    print("New error:", e)
    print("Original error:", e.__cause__)

#Eg7: Built in Exception
 #1. TypeError

try:
    result='100'+4

except TypeError as e:
    print("TypeeError:",e)

# 2. KeyError

try:
    student={"name":"Divya"}
    print(student["age"])

except KeyError as e:
    print("KeyError:", e)

# 3. IndexError

try:
    numbers = [10, 20, 30]
    print(numbers[5])

except IndexError as e:
    print("IndexError:", e)


# 4. FileNotFoundError

try:
    with open ("missing.txt", "r") as file:
        print(file.read())
#Eg7: try-finally without except
except FileNotFoundError as e:
    print("FileNotFoundError:", e)

# 5. NameError

try:
    print(total_amount)

except NameError as e:
    print("NameError:", e)

#Eg6: try-finally without except
try:
    print("Payment processing started")

    result = 10 / 0

    print("Payment successful")

finally:
    print("Payment cleanup completed")





















        
