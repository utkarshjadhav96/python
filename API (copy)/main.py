from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import uvicorn
app = FastAPI()

@app.get('/')

def index():
    return {
        'data':{'name': "sarthak"}
    }

@app.get('/about')
def about():
    return {
        'data':"Wemotive"
    }

@app.get('/blog')

def insert(
    title = str,
    body = str,
    p = bool
):
    return

@app.get('/blog/unpublished')

def unpublished():
    return {"Unnpublished"}

class Blog(BaseModel):
    title : str
    body : str
    published : Optional[bool]


@app.post('/blog')

def create_blog(request:Blog):
    return {'data': f'blog created {request.title}'}


@app.get('/blog/{id}')

def show(id:int):
    return {
        'data': id
    }

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port = 9000)