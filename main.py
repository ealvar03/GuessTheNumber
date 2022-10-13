from art import logo
from structure import number, check_guess


if __name__ == '__main__':
    print(logo)
    print("I'm thinking of a number between 1 and 100.")
    print(f"Psst, the correct answer is {number}")
    check_guess()


