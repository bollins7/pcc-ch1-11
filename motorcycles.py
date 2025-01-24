# Modifying Elements in a list
motorcycles = ['honda', 'yahama', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('harley davidson')
print(motorcycles)

# Making an empty list and adding to it with append
motorcycles = []
motorcycles.append('honda')
motorcycles.append('suzuki')
motorcycles.append('yahama')
print(motorcycles)

# Inserting elements into a list
motorcycles = ['yahama', 'honda', 'suzuki']

motorcycles.insert(0, 'ducati')
print(motorcycles)
motorcycles.insert(2, 'harley davidson')
print(motorcycles)

# Removing an element from a list
del motorcycles[2]
print(motorcycles)

# Removing an item using the pop() method. Removes the top of the list but you can still
# work with it and that is shown by printing the popped_motorcycle 
motorcycles = ['honda', 'yahama', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

# Use the pop() method to print a statement about the last motorcycle owned
last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}")

# Popping items from any position in a list
motorcycles = ['honda', 'yahama', 'suzuki']
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I ever owned was a {first_owned.title()}")

motorcycles.remove('yahama')
print(motorcycles)