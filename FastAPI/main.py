# from fastapi import FastAPI 
# app = FastAPI()

# @app.get("/")
# def read_root():
#     return {"message" : "Hello, Utkarsh !"}

from fastapi import FastAPI
app = FastAPI()

@app.post("/greet")
def greet_user(name:str):
    return {"message" : "Hello ," +name+" !" }

from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/fibonacci/{n}")
def get_fibonacci(n: int):
    if n <= 0:
        return {"error": "n must be a positive integer"}
    sequence = []
    n1 = 0
    n2 = 1
    if n >= 1:
        sequence.append(n1)
    if n >= 2:
        sequence.append(n2)
    for _ in range(n - 2):
        n3 = n1 + n2
        sequence.append(n3)
        n1 = n2
        n2 = n3
    return {"fibonacci_sequence": sequence}

@app.get("/guess/{guess}")
def guess_random(guess: int):
    num = random.randint(1, 10)
    if guess == num:
        result = "Congratulations!!"
    else:
        result = "Not up to mark"
    return {"your_guess": guess, "random_number": num, "result": result}

@app.get("/palindrome/{text}")
def check_palindrome(text: str):
    last = len(text) - 1
    first = 0
    flag = True
    while first < last:
        if text[first] != text[last]:
            flag = False
            break
        first += 1 
        last -= 1 
    
    if flag:
        result = "Palindrome string"
    else:
        result = "Not a palindrome string"
    return {"text": text, "result": result}



