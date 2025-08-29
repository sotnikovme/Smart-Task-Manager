from fapi import FastAPI

app = FastAPI()

@app.post("/register/")
def user_register():
    pass