# app.py
from flask import Flask
from models_forms import db
from routes import routes_bp
from exceptionhandlers import register_error_handlers

# Initialize Flask App
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "mysecretkey"

# Initialize DB inside app.py
db.init_app(app)

# Register Routes & Error Handlers
app.register_blueprint(routes_bp)
register_error_handlers(app)

# Create Tables
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
