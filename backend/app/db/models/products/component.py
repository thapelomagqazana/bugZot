"""
Component model for tracking product components.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.session import Base

class Component(Base):
    """
    Represents product components against which a bug can be filed.
    """
    __tablename__ = "components"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False, unique=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)

    # Relationship with Product (Many-to-One)
    product = relationship("Product", back_populates="components")

    def __repr__(self):
        """Component model representation."""
        return f"<Component {self.name} - Product {self.product_id}>"
