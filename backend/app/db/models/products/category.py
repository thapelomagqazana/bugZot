"""
Category model for product classification.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.session import Base

class Category(Base):
    """
    Represents product categories.
    """
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), unique=True, nullable=False, index=True)

    # Relationship with Products (One-to-Many)
    products = relationship("Product", back_populates="category")

    def __repr__(self):
        """Category model representation."""
        return f"<Category {self.name}>"
