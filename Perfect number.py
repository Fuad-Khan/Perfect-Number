def is_perfect_number(n):
    divisors = [i for i in range(1, n) if n % i == 0]
    return sum(divisors) == n

# Input range from user
start = int(input("Enter the starting number of the range: "))
end = int(input("Enter the ending number of the range: "))

print(f"Perfect numbers between {start} and {end} are:")

# Loop through the range to find perfect numbers
for number in range(start, end + 1):
    if is_perfect_number(number):
        print(number)
