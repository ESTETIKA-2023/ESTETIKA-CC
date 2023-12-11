import uvicorn
from app.api import CreateApp

app = CreateApp()

@app.get("/")
async def root():
    return {"message": "Welcome to ESTETIKA API!"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)