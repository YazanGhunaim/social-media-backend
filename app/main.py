from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import auth, post, user, vote

# models.Base.metadata.create_all(bind=engine) # generate all sqlalchemy tables

origins = ["*"]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)
