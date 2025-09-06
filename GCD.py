def gcd(a, b):
while b:
a, b = b, a % b
return a 
n1 = int(input("Enter one number: ")) # first input number
n2 = int(input("Enter second number: ")) # second input number
print(f"GCD of {n1} and {n2} is {gcd(n1, n2)}") # finding GCD of numbers
