[Youtube vídeo](https://www.youtube.com/watch?v=7t2alSnE2-I)

# First Setps
#### Creating a Venv
```bash
python3 -m venv <venv name>
```

```bash
source <venv name>/binactivate
```
Normaly venv is used as venv name;



#### Instaling FastAPI
```bash
pip install fastapi
```

```bash
pip install uvicorn
```

The command
```bash
uvicorn --version
```
Should return something like
```bash
Running uvicorn 0.23.2 with CPython 3.11.4 on Darwin
```

Run 
```bash
uvicorn main:app --reload
```

#### Create a .gitignore file
```
__pycache__
.venv
.DS_Store
```

### SQL Database
From https://fastapi.tiangolo.com/tutorial/sql-databases/#create-the-pydantic-models


To create a creation route, we need to add a parameter, but if we just add `db` there, FastAPI will understand as a querry parameter.
```py
from sqlalchemy.orm import Session

@app.post("/blog")
def create(blog: schemas.Blog, db: Session):
    return {"data":blog}
```
So, we add the `Session` from `sqlalchemy`. But yet FastAPI don't reconize `Session` as a pydantic type. So we need to add:

```py
from fastapi import Depends

@app.post("/blog")
def create(blog: schemas.Blog, db: Session = Depends(get_db)):
    return {"data":blog}
```

We also needs to define `get_db`:
```py
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()
```


###

Different response codes
https://fastapi.tiangolo.com/tutorial/response-status-code/


To modify reponse status
```py
from fastapi import Response, status

@app.get("/blog/{id}", status_code=status.HTTP_200_OK)
def all(id: int,response: Response, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        response.status_code = status.HTTP_404_NOT_FOUND
        return f"Blog with id {id} was not found."
    return blog
```
Where `status` is responsible for the readable status and `Response` is responsible for the ongoing modification.

Or you can just use:
```py
from fastapi import HTTPException, status

raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} was not found.")
```

### Response model
https://fastapi.tiangolo.com/tutorial/response-model/