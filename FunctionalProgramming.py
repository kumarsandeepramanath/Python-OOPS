print("Functional Programming")

def mutliply_by2(li):
    new_list = []
    for item in li:
        item =  item*2
        new_list.append(item)
    return new_list

print(mutliply_by2([1,2,3]))