from fastapi import FastAPI
import uvicorn

app = FastAPI()

students = [
    {
        "userName": "Nilam",
        "rollNo": 1234
    },
    {
        "userName": "Babita",
        "rollNo": 4567
    }
]

@app.get("/students")
def getStudents():
    return students

@app.post("/addStudent")
def addStudent(userName: str, rollNo: str):
    global students
    students.append({"userName": userName, "rollNo": rollNo})
    return students

# query parameter 
@app.put("/updateStudent")
def updateStudent(rollNo: int, updateName: str):
    print(rollNo, updateName)
    for student in students:
        if student["rollNo"] == rollNo:
            print("updating")
            student["userName"] = updateName
            return {"message": "Student updated", "student": student}
    return {"error": "Student not found"}


@app.delete("/deletestudent")
def deleteStudent(userName: str, rollNo: int):
    global students
    for student in students:
        if student["rollNo"] == rollNo and student["userName"] == userName:
            students.remove(student)
            return {"message": "Student deleted", "student": student}
    return {"error": "Student not found"}


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
