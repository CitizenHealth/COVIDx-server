"""empty message

Revision ID: 703a35d3eea3
Revises: 2f44f27875f2
Create Date: 2020-04-19 19:24:47.747776

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '703a35d3eea3'
down_revision = '2f44f27875f2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('survey_responses', sa.Column('location', sa.String(length=50), nullable=True))
    op.drop_column('users', 'sex')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('sex', mysql.VARCHAR(length=6), nullable=True))
    op.drop_column('survey_responses', 'location')
    # ### end Alembic commands ###