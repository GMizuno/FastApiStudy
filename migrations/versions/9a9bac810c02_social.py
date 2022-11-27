"""social

Revision ID: 9a9bac810c02
Revises: e730ea4c71f1
Create Date: 2022-11-27 18:25:00.135243

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision = '9a9bac810c02'
down_revision = 'e730ea4c71f1'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('social', sa.Column('user_from_id', sa.Integer(), nullable=True))
    op.add_column('social', sa.Column('user_to_id', sa.Integer(), nullable=True))
    op.drop_constraint('social_to_fkey', 'social', type_='foreignkey')
    op.drop_constraint('social_from__fkey', 'social', type_='foreignkey')
    op.create_foreign_key(None, 'social', 'user', ['user_from_id'], ['id'])
    op.create_foreign_key(None, 'social', 'user', ['user_to_id'], ['id'])
    op.drop_column('social', 'to')
    op.drop_column('social', 'from_')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('social', sa.Column('from_', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('social', sa.Column('to', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'social', type_='foreignkey')
    op.drop_constraint(None, 'social', type_='foreignkey')
    op.create_foreign_key('social_from__fkey', 'social', 'user', ['from_'], ['id'])
    op.create_foreign_key('social_to_fkey', 'social', 'user', ['to'], ['id'])
    op.drop_column('social', 'user_to_id')
    op.drop_column('social', 'user_from_id')
    # ### end Alembic commands ###
