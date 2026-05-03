numbers = [1, 2, 4, 5, 7, 8, 10, 11, 13, 14, 15]

for num in numbers[:]:  # iterate over a copy
    if num % 2 == 0:
        numbers.remove(num)

print(numbers)