from sqlalchemy import Column, Integer, ForeignKey
from app.db.session import Base

class RolePermission(Base):
    """
    Association table to map roles to permissions.
    """
    __tablename__ = "role_permissions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    role_id = Column(Integer, ForeignKey("roles.id"), nullable=False)
    permission_id = Column(Integer, ForeignKey("permissions.id"), nullable=False)