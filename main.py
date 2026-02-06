from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Todo API")

# In-memory storage
todos = []

class Todo(BaseModel):
    id: int
    title: str
    completed: bool = False

@app.get("/todos")
def get_todos():
    return todos

@app.post("/todos")
def create_todo(todo: Todo):
    todos.append(todo.dict())
    return todo

@app.get("/")
def root():
    return {"message": "Todo API is running"}