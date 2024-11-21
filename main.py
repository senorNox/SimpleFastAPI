from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Todo(BaseModel):
    id: int
    title: str
    completed: bool = False

todos = []

@app.get("/")
def hello_world():
    return "Hello, world!"

@app.post("/todo")
def create_todo(todo: Todo):
    todos.append(todo)
    return todo

@app.get("/todo")
def get_todos():
    return todos

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)