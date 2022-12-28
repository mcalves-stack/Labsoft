from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import engine
import routers.auth as auth
import routers.user as user
import routers.rooms as rooms
import routers.professores as professores

from models import models

models.Base.metadata.create_all(bind=engine)

 
app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(auth.router)
app.include_router(user.router)
app.include_router(rooms.router)
app.include_router(professores.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}





