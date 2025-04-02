
from flask import Flask
from flask_migrate import Migrate
from models import db
import routes  # Import routes to register them

# Initialize Flask app
app = Flask(__name__)

# Configure the database URI
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///heroes.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  # Disable modification tracking

# Initialize the database and migration
db.init_app(app)
migrate = Migrate(app, db)

# Import routes to ensure they are registered when the app starts
import routes

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
