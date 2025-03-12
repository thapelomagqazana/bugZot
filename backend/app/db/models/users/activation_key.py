"""
Activation Key Model for User Verification.
Stores temporary activation keys for account verification or password resets.
"""

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func, Boolean
from sqlalchemy.orm import relationship
from app.db.session import Base
import uuid

class ActivationKey(Base):
    """
    Model to store activation keys for user account verification.
    """
    __tablename__ = "activation_keys"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    key = Column(String(128), unique=True, nullable=False, default=lambda: str(uuid.uuid4()))
    created_at = Column(DateTime, default=func.now(), nullable=False)
    expires_at = Column(DateTime, nullable=False)
    used = Column(Boolean, default=False, nullable=False)

    # Relationship with User
    user = relationship("User", back_populates="activation_keys")

    def __repr__(self):
        """Activation key model representation."""
        return f"<ActivationKey user_id={self.user_id} key={self.key}>"
