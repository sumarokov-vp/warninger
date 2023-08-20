"""empty message

Revision ID: a27e2352a7fd
Revises: 83bff95e1bfa
Create Date: 2023-08-20 21:16:35.183296

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a27e2352a7fd'
down_revision: Union[str, None] = '83bff95e1bfa'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('warnings', sa.Column('enabled', sa.Boolean(), server_default='1', nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('warnings', 'enabled')
    # ### end Alembic commands ###
