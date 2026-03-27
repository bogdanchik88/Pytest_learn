from fastapi import FastAPI

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
def append(a: int | float, b: int | float):
    return {
        'operation': 'append',
        'first_number': a,
        'second_number': b,
        'result': a - b
    }

@app.get('/api/multiply')
def append(a: int | float, b: int | float):
    return {
        'operation': 'append',
        'first_number': a,
        'second_number': b,
        'result': a * b
    }

@app.get('/api/divide')
def append(a: int | float, b: int | float, div_integer: bool = False):

    result = a // b if div_integer else a / b

    return {
        'operation': 'append',
        'first_number': a,
        'second_number': b,
        'result': result
    }