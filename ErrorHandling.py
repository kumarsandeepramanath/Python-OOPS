while True:
    try :

        age = int(input("Please enter your age"))
        print(f"Age of the person is {age}")
        raise ValueError("Hello boy")
    except ValueError as er:
        print("Please enter a number")
        
    else:
        print("Thanks")
        break
    finally:
        print("I am finally done")