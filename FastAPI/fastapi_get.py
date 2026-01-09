from fastapi import FastAPI
from Fibo import get_fibo
from palindrome import check_palindrome
from guess_num import guess_random

app = FastAPI()

@app.get("/fibonacii/{n}")
def fibo_end(n : int):
    return {"fibonacci series" : get_fibo(n)}

@app.get("/guess/{guess}")
def guess_number(guess: int):
    return guess_random(guess)

@app.get("/palindrome/{txt}")
def palindrome_end(txt :str):
    return check_palindrome(txt)