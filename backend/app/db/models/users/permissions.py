from sqlalchemy import Column, Integer, String
from app.db.session import Base

class Permission(Base):
    """
    Represents individual permissions within the system.
    """
    __tablename__ = "permissions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), unique=True, nullable=False)

    def __repr__(self):
        """Permission model representation."""
        return f"<Permission {self.name}>"
