"""Initial migration

Revision ID: de6d2507e737
Revises: 
Create Date: 2025-06-04 15:20:15.573900

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'de6d2507e737'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('alert_requests',
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('prompt', sa.String(length=511), nullable=False),
    sa.Column('is_recurring', sa.Boolean(), nullable=True),
    sa.Column('max_datetime', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('generic_alerts',
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('content', sa.JSON(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('news_alerts',
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('title', sa.String(length=63), nullable=False),
    sa.Column('content', sa.String(length=2047), nullable=False),
    sa.Column('keywords', sa.JSON(), nullable=False),
    sa.Column('entities', sa.JSON(), nullable=True),
    sa.Column('due_date', sa.DateTime(), nullable=True),
    sa.Column('source_url', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('news_alerts')
    op.drop_table('generic_alerts')
    op.drop_table('alert_requests')
    # ### end Alembic commands ###
