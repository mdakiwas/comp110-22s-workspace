"""This is it, the actual wordle!"""

__author__ = "730474304"


def contains_char(word: str, character: str) -> bool:
    """Returns True when character exists in the word."""
    assert len(character) == 1
    exist: bool = False
    i: int = 0
    while exist is False and i < len(word):
        if word[i] == character:
            exist = True
        else:
            i += 1
    if exist is True:
        return True
    else:
        return False


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def emojified(guess: str, secret: str) -> str:
    """Gives emoji depending whether the guess' letters are in the secret word."""
    assert len(guess) == len(secret)
    i: int = 0
    result: str = ""
    while i < len(secret):
        if guess[i] == secret[i]:
            result += GREEN_BOX
        else:
            if contains_char(secret, guess[i]) is True:
                result += YELLOW_BOX
            else:
                result += WHITE_BOX
        i += 1
    return result


def input_guess(expect_len: int) -> str:
    """Asking for user to guess the secret word."""
    guess: str = input(f"Enter a {expect_len} character word: ")
    while len(guess) != expect_len:
        guess = input(f"That wasn't {expect_len} chars! Try again: ")
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret: str = "codes"
    guess_tries: int = 1
    win: bool = False
    while guess_tries <= 6 and win is False:
        print(f"=== Turn {guess_tries}/6 ===")
        guess: str = input_guess(len(secret))
        emojis: str = emojified(guess, secret)
        print(emojis)
        if guess == secret:
            win = True
        else:
            guess_tries += 1
    if win is True:
        print(f"You won in {guess_tries}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()