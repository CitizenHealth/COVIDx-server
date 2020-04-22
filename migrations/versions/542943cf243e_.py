"""empty message

Revision ID: 542943cf243e
Revises: 4ef7557ddafb
Create Date: 2020-04-22 19:22:15.558640

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '542943cf243e'
down_revision = '4ef7557ddafb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'sex')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('sex', mysql.VARCHAR(length=6), nullable=True))
    # ### end Alembic commands ###