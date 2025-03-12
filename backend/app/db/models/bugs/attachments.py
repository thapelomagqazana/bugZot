"""Model for storing attachments related to bug reports."""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.session import Base

class BugAttachment(Base):
    """Bug attachment model."""

    __tablename__ = "bug_attachments"

    id = Column(Integer, primary_key=True, autoincrement=True)
    bug_id = Column(Integer, ForeignKey("bugs.id"), nullable=False)
    filename = Column(String(255), nullable=False)
    file_url = Column(String(500), nullable=False)

    # Relationships
    bug = relationship("Bug", back_populates="attachments")

    def __repr__(self):
        return f"<BugAttachment {self.filename} for Bug {self.bug_id}>"
