"""empty message

Revision ID: 56d19e0db7f5
Revises: 32e2984fbd7c
Create Date: 2020-04-19 20:54:07.916450

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '56d19e0db7f5'
down_revision = '32e2984fbd7c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('sex', sa.String(length=6), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'sex')
    # ### end Alembic commands ###
