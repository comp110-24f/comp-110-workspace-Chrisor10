"""Creating my own Wordle"""

__author__ = "730654279"


def input_guess(secret_word_len: int) -> str:
    """Ask user for any length character word"""
    while True:
        user_guess: str = input(f"Enter a {secret_word_len} character word: ")
        # using the new concatenation method
        if len(user_guess) == secret_word_len:
            return user_guess
        else:
            print(f"That wasn't {secret_word_len} chars! Try again: {input}")


def contains_char(secret_word: str, char_guess: str) -> bool:
    """Matching chars guess with the secret word"""
    assert len(char_guess) == 1
    idx1: int = 0
    while idx1 < len(secret_word):
        if secret_word[idx1] == char_guess:
            return True
        idx1 = idx1 + 1
    else:
        return False


def emojified(user_guess: str, secret_word: str) -> str:
    """Comparing strings of the guess and the secret word"""
    assert len(user_guess) == len(secret_word)
    white_box: str = "\U00002B1C"
    green_box: str = "\U0001F7E9"
    yellow_box: str = "\U0001f7E8"
    idx_guess: int = 0
    idx_secret: int = 0
    boxes: str = ""
    # using a variable to collect all the emojis into a single string to return
    while idx_guess < len(secret_word):
        if secret_word[idx_secret] == user_guess[idx_guess]:
            boxes = boxes + green_box
        elif contains_char(secret_word, user_guess[idx_guess]) is True:
            # matching the single letter of the guess to the secret word
            boxes = boxes + yellow_box
        else:
            boxes = boxes + white_box
        idx_guess = idx_guess + 1
        idx_secret = idx_secret + 1
    return boxes


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop"""
    num_turns: int = 6
    current_turn: int = 1
    won_game: bool = False
    while current_turn <= num_turns and not won_game:
        print(f" === Turn {current_turn}/{num_turns} === ")
        user_guess: str = input(f"Enter a {len(secret)} character word: ")
        if len(user_guess) < len(secret):
            user_guess: str = input(f"That wasn't {len(secret)} chars! Try again:")
        print(emojified(user_guess, secret))
        if user_guess == secret:
            won_game = True
        else:
            current_turn = current_turn + 1
    if won_game:
        print(f"You won in {current_turn}/{num_turns}! ")
    else:
        print(f"X/{num_turns} -  Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
