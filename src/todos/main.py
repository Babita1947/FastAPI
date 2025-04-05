from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def helloWorld():
    return "Hello, World!"

@app.get("/gettodos")
def getTodos():
    print("Get todos called")
    return "gettodos called"

@app.post("/gettodos")
def getTodosPost():
    print("Get post method todos called")
    return "post gettodos called"

@app.get("/getsingletodo")
def getSingleTodo():
    print("Get SingleTodo called")
    return "getSingleTodo called"

@app.put("/updatetodo")
def updateTodo():
    return "updateTodo called"

# To run the server
def start():
    uvicorn.run("src.todos.main:app", host="127.0.0.1", port=8080, reload=True)
