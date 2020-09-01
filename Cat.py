#Given the below class:
class Cat():
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat1 = Cat('Tom',20)
cat2 = Cat('Dick',30)
cat3 = Cat('Harry',40)

def get_oldest_cat(*args):
        return max(args)

# 2 Create a function that finds the oldest cat
    
print(f"The oldest car is {get_oldest_cat(cat1.age,cat2.age,cat3.age)}")

# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2