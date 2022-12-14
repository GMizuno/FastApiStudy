"""social

Revision ID: a3e0c50ae809
Revises: e9f4adef584a
Create Date: 2022-11-27 18:30:07.888255

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision = 'a3e0c50ae809'
down_revision = 'e9f4adef584a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('social', sa.Column('user_to_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'social', 'user', ['user_to_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'social', type_='foreignkey')
    op.drop_column('social', 'user_to_id')
    # ### end Alembic commands ###
