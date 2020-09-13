# import utility
# from utility import multiply
# import Packaging.packaging
# from Packaging import packaging
import sys
import number_guess

if __name__ =='__main__':
    # print(multiply(2,3))
    # print(packaging.what_is_packaging())

    start_num = sys.argv[1]
    end_num = sys.argv[2]

    while True:
        try:
            current_number = input("Guess a number between 1 and 10 : ")
            print(f"Current number is {current_number}")

            if(int(current_number) == number_guess.generate_random(start_num,end_num)):
                print(f"You have guessed it right my boy!!!!!!!!!!!!!!!!!!!!!!!. Its {current_number}")
                break
            else:
                print("Incorrect guess!! Please try again")
        except ValueError:
            print("Please enter a correct value")

