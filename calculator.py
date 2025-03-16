A = int(input("Enter your no: "))
C = input("enter your operator like +,-,/ and *: ")
B = int(input("Enter your no: "))

if C == "+":
    print(A+B)
elif C == "-":
    print(A-B)
elif C== "/":
    print(A/B if B != 0 else "Error: Division by zero!")
elif C == "*":
    print(A*B)
else:
    print("error occured")

print("Bye Bye!")    