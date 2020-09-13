import random

def generate_random(start_num,end_num):
    print(f"Random number : {random.randint(int(start_num),int(end_num))}")
    return random.randint(int(start_num),int(end_num))