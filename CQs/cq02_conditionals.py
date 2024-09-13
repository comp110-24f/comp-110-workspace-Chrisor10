"""Challenge Question 2"""

__author__ = "730654279"


def guess_a_number() -> None:
    secret: int = 7
    x: str = input("Guess a number: ")
    print("Your guess was " + str(x))
    if int(x) == 7:
        print("You got it!")
    elif int(x) < 7:
        print("Your guess was too low! The secret number is " + str(secret))
    else:
        print("Your guess was too high! The secret number is " + str(secret))


if __name__ == "__main__":
    guess_a_number()
