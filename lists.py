# --- List comprehension ---
# new_list = [expression for member in iterable]
# a list comprehension can work in places you'd use map()
# --------------------------

cubes = []
for num in range(10):
    cubes.append(num * num * num)

print("just the list: ", cubes)

# list comprehension:
cuter_cubes = (num * num * num for num in range(10))
print("list comprehension for cubes")
print(list(cuter_cubes))
