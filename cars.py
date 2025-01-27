cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

# sort in reverse
cars.sort(reverse=True)
print(cars)

# Sorting a list temporarily with the sorted() function
print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)