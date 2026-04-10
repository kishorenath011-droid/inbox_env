from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class EmailInput(BaseModel):
    email: str

@app.post("/reset")
def reset():
    return {"status": "ok"}

@app.post("/run")
def run(data: EmailInput):
    email = data.email.lower()

    if "urgent" in email:
        return {"priority": "high"}
    elif "meeting" in email:
        return {"priority": "medium"}
    else:
        return {"priority": "low"}