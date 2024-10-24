from app import create_app
from app.extensions import db
from app.models.user import User, Role

app = create_app()

@app.cli.command("init-db")
def init_db():
    """Initialize the database with required roles."""
    db.create_all()
    
    # Create roles if they don't exist
    roles = ['farmer', 'buyer', 'admin']
    for role_name in roles:
        if not Role.query.filter_by(name=role_name).first():
            role = Role(name=role_name, description=f'{role_name.capitalize()} role')
            db.session.add(role)
    
    db.session.commit()
    print("Database initialized with roles.")

if __name__ == '__main__':
    app.run(debug=True)