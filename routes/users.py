def add_routes(r, controller):
    r.add_route('/users/', controller.index, 'GET')
    r.add_route('/users/{id}', controller.get, 'GET')
    r.add_route('/users/', controller.create, 'POST')
    r.add_route('/users/{id}', controller.update, 'PUT')
    r.add_route('/users/{id}', controller.delete, 'DELETE')