from fastapi import FastAPI

app = FastAPI()
users = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 17},
    {"name": "Charlie", "age": 25},
]

@app.get("/")
def home():
    return {"message": "Hello World"}
