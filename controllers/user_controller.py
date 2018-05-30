import peewee, json, asyncio
from models.Users import Users

async def index(request):
    users = Users.select().dicts()

    users = [user for user in users]

    return request.Response(json.dumps(users))
async def create(request):
    user_id = Users.insert(request.json).execute()

    return request.Response(json.dumps(retrieve(user_id)))

async def get(request):
    id = request.match_dict['id']

    return request.Response(json.dumps(retrieve(id)))

async def update(request):
    id = request.match_dict['id']

    Users.update(request.json).where(Users.id == id).execute()

    return request.Response(json.dumps(retrieve(id)))
async def delete(request):
    id = request.match_dict['id']

    Users.delete().where(Users.id == id).execute()

    return request.Response('true')

def retrieve(id):
    users = Users.select().where(Users.id == id).dicts()
    users = [user for user in users]

    return users