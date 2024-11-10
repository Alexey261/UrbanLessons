from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def main_page():
    return "Главная страница"

@app.get('/user/admin')
async def admin_page():
    return "Вы вошли как администратор"

@app.get('/user/{user_id}')
async def user_page(user_id: int):
    return f"Вы вошли как пользователь № {user_id}"

@app.get('/user')
async def user_info(user_name: str = "XXX", age: int = 99):
    return f"Информация о пользователе. Имя: '{user_name}', возраст: {age}"