from routes import main_routes
from user.user_routes import user
from blogapp import app

app.register_blueprint(main_routes)
app.register_blueprint(user)
