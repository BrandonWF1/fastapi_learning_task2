from fastapi import *
from fastapi.responses import *
from public.users import users_router

app = FastAPI()

app.include_router(users_router)


@app.get('/', response_class=PlainTextResponse)
def f_index_h():
    content = f"Hello! I am Savva Nesterov from 405th!"
    return content
