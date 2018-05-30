from controllers import user_controller
from routes import users

def add_routes(r):
    users.add_routes(r, user_controller)