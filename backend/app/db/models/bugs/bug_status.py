"""Model representing bug status (e.g., NEW, IN PROGRESS, FIXED)."""

from sqlalchemy import Column, Integer, String
from app.db.session import Base

class BugStatus(Base):
    """Bug status model."""

    __tablename__ = "bug_status"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return f"<BugStatus {self.name}>"
