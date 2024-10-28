# Sum of Odd Numbers
n = int(input("Enter a number: "))

total = 0
for i in range(1,n+1):
    
    # check if number i is odd, if yes add to total
    if i%2 == 1:
        total +=i

print(f"Total of all odd numbers up to {n}: ", total)
    