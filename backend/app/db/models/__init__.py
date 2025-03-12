"""Exports all models from submodules for global use in the application."""

from app.db.models.users import *
from app.db.models.products import *
from app.db.models.bugs import *

__all__ = [
    "User", "Role", "Permission", "ActivationKey", "RolePermission",
    "Product", "Category", "Component", "Version",
    "Bug", "BugStatus", "BugPriority", "BugSeverity", "BugComment", "BugAttachment"
]
