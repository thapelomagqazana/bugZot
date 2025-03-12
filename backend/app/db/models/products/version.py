"""
Version model for tracking product versions.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.session import Base

class Version(Base):
    """
    Represents product versions against which bugs can be categorized.
    """
    __tablename__ = "versions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    version_name = Column(String(50), nullable=False, index=True)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)

    # Relationship with Product (Many-to-One)
    product = relationship("Product", back_populates="versions")

    def __repr__(self):
        """Version model representation."""
        return f"<Version {self.version_name} - Product {self.product_id}>"
