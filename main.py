from fastapi import FastAPI
from database import Base, engine

# Setting up tables for database
Base.metadata.create_all(bind=engine)

app = FastAPI()

from api.comments_api import comments
from api.photo_api import photos
from api.posts_api import post
from api.users_api import users
from api.hashtags_api import hashtags
