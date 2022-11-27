"""social

Revision ID: a1e65dc79adb
Revises: 9a9bac810c02
Create Date: 2022-11-27 18:26:07.889068

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision = 'a1e65dc79adb'
down_revision = '9a9bac810c02'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('social_user_to_id_fkey', 'social', type_='foreignkey')
    op.drop_column('social', 'user_to_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('social', sa.Column('user_to_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('social_user_to_id_fkey', 'social', 'user', ['user_to_id'], ['id'])
    # ### end Alembic commands ###
