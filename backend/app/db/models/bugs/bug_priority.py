"""Model representing bug priority (e.g., P1, P2, P3)."""

from sqlalchemy import Column, Integer, String
from app.db.session import Base

class BugPriority(Base):
    """Bug priority model."""

    __tablename__ = "bug_priority"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return f"<BugPriority {self.name}>"
