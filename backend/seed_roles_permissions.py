import sys
import datetime
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from app.db.models.users import Role, Permission, User
from app.core.config import settings

# Database connection URL (Modify if necessary)
DATABASE_URL = settings.SQL_URL

# Create engine and session
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

# Define Roles
roles_data = [
    {"name": "Admin"},
    {"name": "User"},
    {"name": "Developer"},
    {"name": "QA"},
    {"name": "Support"},
]

# Define Permissions
permissions_data = [
    {"name": "view_users"},
    {"name": "edit_users"},
    {"name": "delete_users"},
    {"name": "create_bug"},
    {"name": "edit_bug"},
    {"name": "delete_bug"},
    {"name": "manage_roles"},
    {"name": "view_reports"},
]

# Mapping Roles to Permissions
role_permissions_mapping = {
    "Admin": ["view_users", "edit_users", "delete_users", "manage_roles", "view_reports"],
    "User": ["view_users", "create_bug"],
    "Developer": ["view_users", "edit_bug", "view_reports"],
    "QA": ["view_users", "create_bug", "edit_bug", "view_reports"],
    "Support": ["view_users", "view_reports"],
}

try:
    # Insert Roles
    for role_data in roles_data:
        role = Role(name=role_data["name"])
        session.add(role)
    session.commit()

    # Insert Permissions
    for perm_data in permissions_data:
        permission = Permission(name=perm_data["name"])
        session.add(permission)
    session.commit()

    # Assign Permissions to Roles
    roles = {role.name: role for role in session.query(Role).all()}
    permissions = {perm.name: perm for perm in session.query(Permission).all()}

    for role_name, perm_names in role_permissions_mapping.items():
        role = roles.get(role_name)
        if role:
            role.permissions = [permissions[perm] for perm in perm_names if perm in permissions]
            session.add(role)
    
    session.commit()
    print("✅ Roles and Permissions seeded successfully!")

except Exception as e:
    session.rollback()
    print(f"❌ Error seeding roles and permissions: {str(e)}", file=sys.stderr)

finally:
    session.close()
