from fastapi import FastAPI, Path
from typing_extensions import Annotated  # sorry for Python 3.8

app = FastAPI()

@app.get('/')
async def main_page():
    return "Главная страница"

#  ============= CRUD requests ==================

users = {'1': 'Имя: Example, возраст: 18'}

@app.get('/users')
async def get_all_users() -> dict:
    return users

@app.post('/user/{username}/{age}')
async def add_user(username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser')],
                    age: Annotated[int, Path(ge=18, le=120, description="Enter age", example='24')]) -> str:
    user_id = str(int(max(users, key=int))+1)
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f"User {user_id} is registered"

@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: Annotated[int, Path(ge=1, le=100, description="Enter User ID", example='1')],
                      username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser')],
                      age: Annotated[int, Path(ge=18, le=120, description="Enter age", example='24')]) -> str:
    users[str(user_id)] = f'Имя: {username}, возраст: {age}'
    return f"User {user_id} is updated"

@app.delete('/user/{user_id}')
async def delete_user(user_id: int = Path(ge=1, le=100, description="Enter User ID", example='1')) -> str:
    users.pop(str(user_id))
    return f"User {user_id} has been deleted"
