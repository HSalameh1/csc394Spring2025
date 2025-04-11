from fastapi import FastAPI

app = FastAPI()

workout_list = ["abs"]

@app.get("/workout")
async def get_strings():
    return {"workout": workout_list}

@app.post("/workout")
async def add_string(name: str = ""):
    workout_list.append(name)
    return {"workout": workout_list}

@app.delete("/workout")
async def delete_string(index: int = 0):
    workout_list.pop(index)
    return {"workout": workout_list}

