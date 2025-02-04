from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import datetime
from datetime import datetime, timezone


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
        "email": "judeliisent@gmail.com",
        "current_datetime": datetime.utcnow().isoformat() + "Z",

        "github_url": "https://github.com/UgoBest100/HNG-TASK-ONE"
    }