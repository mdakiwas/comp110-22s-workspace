"""I choose you, wordle! GO!"""

__author__ = "730474304"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
secret: str = "python"
guess: str = input(f"What is your {len(secret)}-letter guess? ")  # asking user input for a word guess

while len(guess) != len(secret): 
    guess: str = input(f"That was not {len(secret)} letters! Try again: ")  # re-asking user input if length is wrong

i: int = 0
result: str = "" 
while i < len(guess):
    if guess[i] == secret[i]:  # green emoji for correct letter in correct placement
        result += GREEN_BOX
    else:
        exist: bool = False
        alt_i: int = 0
        while exist is False and alt_i < len(secret):  # yellow emoji for existing letter in wrong placement
            if secret[alt_i] == guess[i]:
                exist = True
            else:
                alt_i += 1    
        if exist is True:
            result += YELLOW_BOX
        else:
            result += WHITE_BOX  # white emoji for wrong letter   
    i += 1

print(result)
if guess != secret: 
    print("Not quite. Play again soon!")
else:
    print("Woo! You got it!")