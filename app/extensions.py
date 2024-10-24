from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_security import Security
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
security = Security()
migrate = Migrate()
mail = Mail()
ma = Marshmallow() #To remove this as new version on flask marshmallow is not compatible with this