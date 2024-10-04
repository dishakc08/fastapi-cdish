from fastapi import FastAPI, Response

app = FastAPI()

@app.get("/ping")
def health_check():
    return Response(content="healthy", status_code=200)

