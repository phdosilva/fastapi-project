from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn


app = FastAPI()


@app.get("/blog")
def index(limit: int = 10, published: bool = True, sort: Optional[str] = None):
    return {"data": {"limit": limit, "published": published}}

@app.get("/blog/unpublished")
def unpublished():
    return {"data": "all unpublished blogs"}

@app.get("/blog/{id}")
def show(id: int):
    return {"data": id}

@app.get("/blog/{id}/comments")
def comments(id: int):
    return {"data": ["1", "2"]}

 
class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@app.post("/blog")
def create(blog: Blog):
    return {"data": f"blog created with title as {blog.title}"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port="8000")
