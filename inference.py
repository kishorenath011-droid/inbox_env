from fastapi import FastAPI, Request

app = FastAPI()

@app.api_route("/", methods=["GET", "POST"])
async def root(request: Request):
    try:
        data = await request.json()
    except:
        data = {}

    email = str(data).lower()

    if "urgent" in email:
        return {"priority": "high"}
    elif "meeting" in email:
        return {"priority": "medium"}
    else:
        return {"priority": "low"}

@app.api_route("/{path:path}", methods=["GET", "POST"])
async def catch_all(path: str, request: Request):
    return {"status": "ok"}