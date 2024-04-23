from fastapi import FastAPI;
from pydantic import BaseModel;
from typing import Text,Optional;
from datetime import datetime;

app = FastAPI()
posts = []

#post model
class Post(BaseModel):
    id:int
    title:str
    author:str
    content:Text
    created_at:datetime = datetime.now()
    published_at:Optional[datetime]
    isPuublished:bool = False
    

@app.get('/')
def homepage():
    return{'welcome':'welcome to my REST API'}

@app.get('/posts')
def get_post():
    return posts

@app.post('/')
def save_post(post: Post):
    for i in posts:
        if post.id == i['id']:
            return print('is Set')
    posts.append(post.dict()) 
    print('posts =>',posts[len(posts)-1])