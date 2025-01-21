from fastapi import FastAPI

app = FastAPI()


@app.get("/api/say_hello")
async def say_hello():
    return {"Hello World - First GET"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0,0,0,0", port=8080)
