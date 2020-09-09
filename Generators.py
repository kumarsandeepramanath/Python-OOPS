print("Generators")

def generate_values(num):
    for i in range(num):
        yield i

# for item in generate_values(1000):
#     print(item)

g = generate_values(1000)
# next(g)
# next(g)
print(next(g))
print(next(g))
print(next(g))
