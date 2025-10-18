age = int(input("Enter your age: "))

if age > 120:
    print("Invalid age")
elif age >= 18:
    print("You are an adult")
elif age >= 13:
    print("You are a teenager")
else:
    print("You are a child")
