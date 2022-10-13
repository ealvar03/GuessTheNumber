from art import logo
import structure


if __name__ == '__main__':
    print(logo)
    print("I'm thinking of a number between 1 and 100.")
    print(f"Psst, the correct answer is {structure.number}")
    structure.check_guess()


