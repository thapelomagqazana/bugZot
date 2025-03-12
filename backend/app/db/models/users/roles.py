from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.session import Base

class Role(Base):
    """
    Represents user roles (Admin, Developer, Tester, etc.).
    """
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), unique=True, nullable=False)
    
    # Relationship with User
    users = relationship("User", back_populates="role")

    # Relationship with Permissions
    permissions = relationship("Permission", secondary="role_permissions", backref="roles")

    def __repr__(self):
        """Role model representation."""
        return f"<Role {self.name}>"
