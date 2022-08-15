from fastapi import HTTPException
from fastapi import FastAPI
from database import database as connection
from database import User
from schemas import UserRequestModel
from schemas import UserResponseModel

app = FastAPI(title= "Live de CF", description="Prueba de FastAPI", version= "1.0.1")

@app.on_event('startup')
def startup():
    if connection.is_closed():
        connection.connect()
    connection.create_tables(models=[User])

@app.on_event('shutdown')
def shutdown():
    if not connection.is_closed:
        connection.close()

@app.get('/users')
async def list_user():
    pass

@app.post('/users')
async def create_user(user: UserRequestModel):
    user = User.create(
        username = user.username,
        email = user.email
    )
    return user

@app.get('/users/{user_id}')
async def get_user(user_id):
    user = User.select().where(User.id== user_id).first()
    if user:
        return UserResponseModel(
            id= user.id,
            username= user.username,
            email= user.email
        )
    else:
        return HTTPException(404, "User not found")

@app.put('/users/{user_id}')
async def update_user(user_id):
    user = User.select().where(User.id== user_id).first()
    
@app.delete('/users/{user_id}')
async def delete_user(user_id):
    user = User.select().where(User.id== user_id).first()
    if user:
        user.delete_instance()
    else:
        return HTTPException(404, "User not found")