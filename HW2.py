from fastapi import FastAPI

app = FastAPI()

workout_list = []
meal_list = []
user_list = []

#list of workouts 
@app.get("/workouts")
async def get_workouts():
    return {"workouts": workout_list}

@app.post("/workouts")
async def add_workout(name: str = ""):
    workout_list.append(name)
    return {"workouts": workout_list}

@app.delete("/workouts")
async def delete_workout(index: int = 0):
    workout_list.pop(index)
    return {"workouts": workout_list}

#list of meals 
@app.get("/meals")
async def get_meals():
    return {"meals": meal_list}

@app.post("/meals")
async def add_meal(name: str = ""):
    meal_list.append({"name": name})
    return {"meals": meal_list}

@app.delete("/meals")
async def delete_meal(index: int = 0):
    meal_list.pop(index)
    return {"meals": meal_list}

#list of users 
@app.get("/users")
async def get_users():
    return {"users": user_list}

@app.post("/users")
async def add_user(name: str = "", age: int = 0):
    user_list.append({"name": name, "age": age})
    return {"users": user_list}

@app.delete("/users")
async def delete_user(index: int = 0):
    user_list.pop(index)
    return {"users": user_list}