"""
Lamba, Map, filter and reduce are high order functions of Python. I will demonstrate each of these functions with many examples.
"""

# In this example. I want to cube all the numbers in a list. So I created my function to cube numbers.
def cubed(x):
    return x**3

# print(cubed(3))
# Created list with numbers in them
nums = [3, 4, 5, 6, 7, 8, 9]

# Created a variable that explicitly states that this is a list. Then I used the map function with two arguments.
# The function I created and then the target which is my nums list.
result = list(map(cubed, nums))
# print(result)

def squared(x):
    return x**2

nums2 = [10, 11, 12, 13, 14, 15]
result = list(map(squared, nums2))

# print(result)

# Using a map filter with converting strings to numbers.
alpha_list = ['a', 'b', 'c', 'd', 'w', 'x', 'y', 'z']
alpha_to_num = list(map(ord, alpha_list))
# print(f'This is my alpha list converting to numbers {alpha_to_num}')

# Experiment
# Can this map function work with a string like "Hello world!"?

my_string = "Hello world"
new_string = list(map(ord, my_string))
# print(f'Hello world into this: {new_string}') # It can if you convert the string into a list

conver_back = list(map(chr, new_string))
# print(f'Numbers back to string: {conver_back}')


"""
Filter: A function that filters an iterable by returning items that return true.
"""

nums3 = [1,2,3,4,5,6,7,8,9]
nums4 = [23, 20, 48, 49, 71, 72]
res = list(filter(lambda x: x%2==0, nums3))
print(nums, res) # prints out numbers that are divisible by 2 evenly. 

num5 = [1,2,5,8,3,0,7]
res2 = list(filter(lambda x: x < 5, num5))
print(num5, res2) # returns all numbers smaller than 5

# Filtering through a list of dicts
my_dict = {}

"""
Reduce: 
"""