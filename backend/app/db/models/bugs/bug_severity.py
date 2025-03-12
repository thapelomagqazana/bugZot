"""Model representing bug severity (e.g., Critical, Major, Minor)."""

from sqlalchemy import Column, Integer, String
from app.db.session import Base

class BugSeverity(Base):
    """Bug severity model."""

    __tablename__ = "bug_severity"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return f"<BugSeverity {self.name}>"
