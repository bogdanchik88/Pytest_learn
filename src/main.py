from fastapi import FastAPI, HTTPException

app = FastAPI(
    title='Super Puper App'
)

@app.get('/api')
def health():
    return {'message': 'hello fastapi'}

@app.get('/api/append')
def append(a: int | float, b: int | float):
    return {
        'operation': 'append',
        'first_number': a,
        'second_number': b,
        'result': a + b
    }

@app.get('/api/substract')
def substract(a: int | float, b: int | float):
    return {
        'operation': 'substract',
        'first_number': a,
        'second_number': b,
        'result': a - b
    }

@app.get('/api/multiply')
def multiply(a: int | float, b: int | float):
    return {
        'operation': 'multiply',
        'first_number': a,
        'second_number': b,
        'result': a * b
    }

@app.get('/api/divide')
def divide(a: int | float, b: int | float, div_integer: bool = False):

    if b == 0:
        raise HTTPException(status_code=400, detail='Cannot divide by zero!')

    result = a // b if div_integer else round(a / b, 2)

    return {
        'operation': 'divide',
        'first_number': a,
        'second_number': b,
        'result': result
    }