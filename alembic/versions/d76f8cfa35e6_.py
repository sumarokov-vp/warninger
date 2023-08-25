"""empty message

Revision ID: d76f8cfa35e6
Revises: 9db5ad4bdfb2
Create Date: 2023-08-23 12:00:12.557690

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd76f8cfa35e6'
down_revision: Union[str, None] = '9db5ad4bdfb2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('warning_status',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('warning_id', sa.Integer(), nullable=True),
    sa.Column('success', sa.Boolean(), server_default='0', nullable=True),
    sa.Column('datetime', sa.DateTime(), nullable=True),
    sa.Column('message', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['warning_id'], ['warnings.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('warning_status')
    # ### end Alembic commands ###