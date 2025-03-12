"""Model representing comments on bug reports."""

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from app.db.session import Base
from sqlalchemy.sql import func

class BugComment(Base):
    """Bug comment model."""

    __tablename__ = "bug_comments"

    id = Column(Integer, primary_key=True, autoincrement=True)
    bug_id = Column(Integer, ForeignKey("bugs.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    # Relationships
    bug = relationship("Bug", back_populates="comments")
    user = relationship("User", lazy="joined")

    def __repr__(self):
        return f"<BugComment by {self.user.username} on Bug {self.bug_id}>"
