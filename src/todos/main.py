from fastapi import FastAPI
import uvicorn

app = FastAPI()

students = [
    {
        "userName": "Nilam",
        "rollno": 1234
    },
    {
        "userName": "Babita",
        "rollno": 4567
    }
]

@app.get("/students")
def getStudents():
    return students

@app.get("/addStudent")
def addStudent(userName: str, rollNo: str):
    global students
    students.append({"userName": userName, "rollNo": rollNo})
    return students

@app.get("/")
def helloWorld():
    return "Hello, World!"

@app.get("/gettodos/{id}")
def getTodos(id):
    print("Get todos called", id)
    return id

@app.post("/gettodos")
def getTodosPost():
    print("Get post method todos called")
    return "post gettodos called"

# Dynamic Query Parameters

@app.get("/getsingletodo")
def getSingleTodo(userName: str, rollNo: str):
    print("Get SingleTodo called", userName, rollNo)
    return "getSingleTodo called"

@app.put("/updatetodo")
def updateTodo():
    return "updateTodo called"

# Dynamic Path parameters

@app.get("/name/{first_name}/{last_name}")
def get_full_name(first_name:str, last_name:str):
    full_name = first_name.title() + " " + last_name.title()
    return full_name

print(get_full_name("john", "doe"))



# To run the server
def start():
    uvicorn.run("src.todos.main:app", host="127.0.0.1", port=8080, reload=True)
