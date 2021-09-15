from fastapi import FastAPI


app = FastAPI(title="Jobboard", varion="0.0.1")


@app.get("/")
def hello_api():
    return {"message": "Hello World!"}
