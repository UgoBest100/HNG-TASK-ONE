from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import datetime

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {
        "email": "judelisent@gmail.com",
        "current_datetime": datetime.datetime.now(datetime.UTC).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "github_url": "https://github.com/UgoBest100/HNG-TASK-ONE"
    }