# define a simple function
def sum_values(a, b):
    return a + b

print(sum_values(9, 1))

# useful built in functions

countries = ['us', 'can', 'aus', 'chin']

print(len(countries))

# min/max
print(min([1, 2, 5, 10, 8]))
print("max: " + str(max([1, 2, 5, 10, 8])))

# range
print("range 0 to 16 by 3's:")
for i in range(0, 16, 3):
    print(i)
