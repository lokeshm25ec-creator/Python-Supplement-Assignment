numbers = [10, 20, 30, 40, 50]
search = 30
index = -1

for i in range(len(numbers)):
    if numbers[i] == search:
        index = i
        break   # stop searching once found

print(f"Index of {search}: {index}")

