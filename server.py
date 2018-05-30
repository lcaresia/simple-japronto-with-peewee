from japronto import Application
from routes import routes

app = Application()

routes.add_routes(app.router)

app.run(debug=True)