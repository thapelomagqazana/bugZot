"""
User data model for storing user account information.
The model is responsible for storing the account information on a
per-user basis and providing access to it for authentication purposes.
"""

from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.db.session import Base
from datetime import datetime

class User(Base):
    """
    User model representing registered users.
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    password = Column(String(512), nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    
    user_role = Column(Integer, ForeignKey("roles.id"), nullable=False)
    role = relationship("Role", lazy=False)  # Directly fetch role information

    joining_date = Column(DateTime, nullable=False, default=datetime.utcnow)
    last_login = Column(DateTime, nullable=True, onupdate=datetime.utcnow)
    account_status = Column(Boolean, nullable=False, default=False)

    # Activation keys for email verification
    activation_keys = relationship("ActivationKey", back_populates="user")
    
    def __repr__(self):
        """User model representation."""
        return f"<User {self.username}>"
