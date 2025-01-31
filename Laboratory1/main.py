from fastapi import FastAPI

app = FastAPI()

@app.get("/factorial/{starting_number}")
def factorial(starting_number: int):
    if starting_number == 0:
        return {"return": False}

    result = 1
    number = starting_number

    while number > 1:
        result *= number
        number -= 1

    return {"starting_number": starting_number, "factorial": result}