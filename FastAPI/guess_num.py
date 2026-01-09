
import random
def guess_random(guess: int):

    num = random.randint(1,10)

    if guess == num:
        result = "Congratulations!!"
    else:
        result = "Incorrect Guess !!"
    return {"Your Guess": guess, "Random Number " :num, "result" :result }