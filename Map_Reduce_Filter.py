from functools import reduce

#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']

def capitalize_pets(item):
    return item.capitalize()

print(list(map(capitalize_pets,my_pets)))

#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]

# print(list(sorted(zip(my_strings,my_numbers))))
print(list(zip(my_strings,my_numbers)))

#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]

def get_good_scores(item):
    return item>50

print(list(filter(get_good_scores,scores)))


#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). 
# What is the total?
my_numbers = my_numbers+scores

def get_total(acc,item):
    return acc+item

print(reduce(get_total,my_numbers,0))

print(list(map(lambda item: item*2,scores)))

my_list = [5,4,3]
print(list(map(lambda item: item*item,my_list)))

a= [(0,2),(4,3),(9,9),(10,-1)] 
# print(list(map(lambda item: item,sorted(a))))

num_list = [num.capitalize() for num in 'hello']
print(num_list)
