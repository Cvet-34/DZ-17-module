#В файле main.py создайте сущность FastAPI(), напишите один маршрут для неё - '/',
#по которому функция возвращает словарь - {"message": "Welcome to Taskmanager"}.
#Импортируйте объекты APIRouter и подключите к ранее созданному приложению FastAPI,
#объединив все маршруты в одно приложение.


#Строим базовую структуру
from fastapi import FastAPI
from routerss import user
from routerss import task


app = FastAPI()

@app.get("/")
async def welcome():
    return {"message": "Welcome to Taskmanager"}

app.include_router(user.router) # Это позволит нам подключать внешние роутеры и массштабировать приложения
app.include_router(task.router)