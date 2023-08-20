"""empty message

Revision ID: 837015d1e827
Revises: a8e70aa33464
Create Date: 2023-08-20 16:09:26.405461

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '837015d1e827'
down_revision: Union[str, None] = 'a8e70aa33464'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('chat_id_unique', 'users', ['chat_id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('chat_id_unique', 'users', type_='unique')
    # ### end Alembic commands ###
