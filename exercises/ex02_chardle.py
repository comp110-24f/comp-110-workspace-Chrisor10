"""Ex02 - Chardle Exercise"""

__author__ = "730654279"


def input_word() -> str:
    """Ask user for a 5 character word"""
    user_word_input: str = input("Enter a 5-character word: ")
    if len(user_word_input) == 5:
        return user_word_input
    else:
        print("Error: Word must contain 5 characters.")
        exit()  # exits the programs to not continue running


def input_letter() -> str:
    user_letter_input: str = input("Enter a single character: ")
    if len(user_letter_input) == 1:
        return user_letter_input
    else:
        print("Error: Character must be a single character.")
        exit()  # exits the programs to not continue running


def contains_char(word: str, letter: str) -> None:
    print("Searching for " + letter + " in " + word)
    index: int = 0
    count: int = 0
    while index < len(word):
        if word[index] == letter:
            print(letter + " found at index " + str(index))
            count = count + 1  # increment for counting each match
        index = index + 1  # to make sure the loop increases and doesn't go to infinity
    if count == 0:
        print("No instances of " + letter + " found in " + word)
    elif count == 1:
        print(str(count) + " instance of " + letter + " found in " + word)
    else:
        print(str(count) + " instances of " + letter + " found in " + word)


def main() -> None:
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()
