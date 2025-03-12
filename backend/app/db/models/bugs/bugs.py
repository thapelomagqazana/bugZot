"""Bug model definition.

This model is used to store information related to reported bugs in the system.
"""

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from app.db.session import Base
from sqlalchemy.sql import func

class Bug(Base):
    """Model representing a reported bug in the system."""
    
    __tablename__ = "bugs"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False, index=True)
    description = Column(Text, nullable=False)
    status_id = Column(Integer, ForeignKey("bug_status.id"), nullable=False)
    priority_id = Column(Integer, ForeignKey("bug_priority.id"), nullable=False)
    severity_id = Column(Integer, ForeignKey("bug_severity.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    component_id = Column(Integer, ForeignKey("components.id"), nullable=True)
    version_id = Column(Integer, ForeignKey("versions.id"), nullable=True)
    reporter_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    assigned_to_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), nullable=False)

    # Relationships
    status = relationship("BugStatus", lazy="joined")
    priority = relationship("BugPriority", lazy="joined")
    severity = relationship("BugSeverity", lazy="joined")
    product = relationship("Product", lazy="joined")
    component = relationship("Component", lazy="joined")
    version = relationship("Version", lazy="joined")
    reporter = relationship("User", foreign_keys=[reporter_id], lazy="joined")
    assigned_to = relationship("User", foreign_keys=[assigned_to_id], lazy="joined")
    comments = relationship("BugComment", back_populates="bug", cascade="all, delete")
    attachments = relationship("BugAttachment", back_populates="bug", cascade="all, delete")

    def __repr__(self):
        return f"<Bug {self.title} - Status: {self.status.name}>"
