# my_file = open('book.txt')
# print(my_file.readline())
# my_file.seek(0)
# print(my_file.readlines())
# my_file.seek(0)
# print(my_file.read())

# my_file.close()

# with open('book.txt') as my_file:
#     print(my_file.readlines())

# with open('book.txt',mode='a') as my_file:
#     my_file.write("Hello All, Python is interesting!!!")

with open('new_book.txt',mode='a') as my_file:
    my_file.write("Hello All, Python is interesting!!!")