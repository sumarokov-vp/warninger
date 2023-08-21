"""empty message

Revision ID: 9a42ac495456
Revises: a27e2352a7fd
Create Date: 2023-08-21 20:23:58.313775

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9a42ac495456'
down_revision: Union[str, None] = 'a27e2352a7fd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('warnings', sa.Column('name', sa.String(), nullable=True))
    op.add_column('warnings', sa.Column('description', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('warnings', 'description')
    op.drop_column('warnings', 'name')
    # ### end Alembic commands ###