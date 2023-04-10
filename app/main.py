from fastapi import fastAPI

app = fastAPI()

@app.get("/")
async def root():
    return {"message": "Hey Actions"}