from fastapi import FastAPI, Request, Body
import uvicorn
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import users
from funcDB import MongoDB



app = FastAPI()
app.mount('/static', StaticFiles(directory='static'), name='static')
templates = Jinja2Templates(directory='templates')

db = MongoDB(database_name='edu', uri='mongodb://127.0.0.1:27017/')

app.include_router(
    users.router,
    prefix='/users',
    tags= ['users'],
    responses={
        401: {'description': 'error'}
    }
)

@app.get('/')
async def root_user(request: Request):
    return templates.TemplateResponse('home.html', context={'request':request})

@app.post("/")
async def homepost():
    return {'message':"success"}

@app.get("/testtable")
async def testtable(request: Request):
    return templates.TemplateResponse('table.html', context={'request':request})


if __name__ == "__main__":
    uvicorn.run('app:app', debug=True)