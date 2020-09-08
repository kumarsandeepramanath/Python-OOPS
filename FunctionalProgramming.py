print("Functional Programming")

def mutliply_by2(li):
    new_list = []
    for item in li:
        item =  item*2
        new_list.append(item)
    return new_list

def mutliply_by2(item):
    return item*2
print(list(map(mutliply_by2,[1,2,3])))
# print(mutliply_by2([1,2,3]))

def check_if_odd(item):
    return item%2 ==1

print(list(filter(check_if_odd,[1,2,3])))