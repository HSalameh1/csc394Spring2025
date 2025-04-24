import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from openai import OpenAI

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

app = FastAPI()

# Sample data
workout_list = ["abs", "squats", "arms"]
meal_list = ["salad"]
user_workouts = {
    1: ["arms", "abs", "squats"],
    2: ["cardio", "legs", "yoga"],
    3: ["arms", "arms", "abs"]
}
user_list = []

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

@app.get("/meals")
async def get_meals():
    return {"meals": meal_list}

@app.post("/meals")
async def add_meal(name: str = ""):
    meal_list.append(name)
    return {"meals": meal_list}

@app.delete("/meals")
async def delete_meal(index: int = 0):
    meal_list.pop(index)
    return {"meals": meal_list}

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

@app.get("/suggest_workout")
async def suggest_workout(user_id: int = 0):
    if user_id not in user_workouts:
        raise HTTPException(status_code=404, detail="User not found")
    try:
        prompt = build_prompt(user_id)
        client = OpenAI(api_key=api_key)
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return {"suggested_workout": response.choices[0].message.content.strip()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def build_prompt(user_id):
    previous = ", ".join(user_workouts[user_id])
    prompt = f"""Based on this workout history: {previous}, suggest a next workout.
    Keep it short and in a list format. Only return the workout name."""
    print("Prompt sent to OpenAI:", prompt)
    return prompt