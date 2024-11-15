from fastapi import FastAPI
import debugpy

app = FastAPI()
debugpy.listen(("0.0.0.0", 5678))

@app.get("/")
def root():
     return {"message": "Hello World"}