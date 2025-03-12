"""
Product definition model.
Stores information related to products for which users can file a bug.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.session import Base

class Product(Base):
    """
    Represents a product for which users can file a bug.
    """
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, autoincrement=True)
    product_name = Column(String(100), nullable=False, unique=True, index=True)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=True)

    # Relationship with Category (Many-to-One)
    category = relationship("Category", back_populates="products")

    # Relationship with Components and Versions (One-to-Many)
    components = relationship("Component", back_populates="product", cascade="all, delete")
    versions = relationship("Version", back_populates="product", cascade="all, delete")

    def __repr__(self):
        """Product model representation."""
        return f"<Product {self.product_name}>"
