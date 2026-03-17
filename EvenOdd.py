even = 0
odd = 0

for i in range(5):
    num = int(input("Enter number: "))
    
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even numbers:", even)
print("Odd numbers:", odd)