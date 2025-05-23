"""Add user_id to transactions

Revision ID: c4163e4f69cc
Revises: 7736dbd5137f
Create Date: 2025-03-01 00:59:04.961373

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c4163e4f69cc'
down_revision: Union[str, None] = '7736dbd5137f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('transactions_user_id_fkey', 'transactions', type_='foreignkey')
    op.drop_column('transactions', 'user_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('transactions', sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('transactions_user_id_fkey', 'transactions', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###
