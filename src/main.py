from fastapi import FastAPI

app = FastAPI(
    title='Super Puper App'
)

@app.get('/')
def health():
    return {'message': 'hello fastapi'}

