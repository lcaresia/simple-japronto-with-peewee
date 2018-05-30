from japronto import Application
from controllers import user_controller

app = Application()

r = app.router

# USUARIOS
r.add_route('/users/', user_controller.index, 'GET')
r.add_route('/users/{id}', user_controller.get, 'GET')
r.add_route('/users/', user_controller.create, 'POST')
r.add_route('/users/{id}', user_controller.update, 'PUT')
r.add_route('/users/{id}', user_controller.delete, 'DELETE')

app.run(debug=True)