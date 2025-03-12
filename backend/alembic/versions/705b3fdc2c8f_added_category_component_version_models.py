"""Added Category, Component, Version models

Revision ID: 705b3fdc2c8f
Revises: abbec5feb6a6
Create Date: 2025-03-12 18:06:58.220000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '705b3fdc2c8f'
down_revision: Union[str, None] = 'abbec5feb6a6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema by handling dependencies properly."""
    
    # Drop constraints before dropping dependent tables
    op.drop_constraint('activation_keys_user_id_fkey', 'activation_keys', type_='foreignkey')
    op.drop_constraint('users_user_role_fkey', 'users', type_='foreignkey')
    op.drop_constraint('role_permissions_role_id_fkey', 'role_permissions', type_='foreignkey')
    op.drop_constraint('role_permissions_permission_id_fkey', 'role_permissions', type_='foreignkey')

    # Drop tables in correct order
    op.drop_table('activation_keys')
    op.drop_table('role_permissions')
    op.drop_table('permissions')
    op.drop_table('users')
    op.drop_table('roles')


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('users_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('username', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('password', sa.VARCHAR(length=512), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('user_role', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('joining_date', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('last_login', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('account_status', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['user_role'], ['roles.id'], name='users_user_role_fkey'),
    sa.PrimaryKeyConstraint('id', name='users_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_index('ix_users_username', 'users', ['username'], unique=True)
    op.create_index('ix_users_email', 'users', ['email'], unique=True)
    op.create_table('activation_keys',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('key', sa.VARCHAR(length=128), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('expires_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('used', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='activation_keys_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='activation_keys_pkey'),
    sa.UniqueConstraint('key', name='activation_keys_key_key')
    )
    op.create_table('role_permissions',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('role_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('permission_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['permission_id'], ['permissions.id'], name='role_permissions_permission_id_fkey'),
    sa.ForeignKeyConstraint(['role_id'], ['roles.id'], name='role_permissions_role_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='role_permissions_pkey')
    )
    op.create_table('permissions',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='permissions_pkey'),
    sa.UniqueConstraint('name', name='permissions_name_key')
    )
    op.create_table('roles',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='roles_pkey'),
    sa.UniqueConstraint('name', name='roles_name_key')
    )
    # ### end Alembic commands ###
