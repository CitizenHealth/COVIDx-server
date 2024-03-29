"""empty message

Revision ID: 4ef7557ddafb
Revises: 33aa7aac986c
Create Date: 2020-04-22 19:19:54.543317

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4ef7557ddafb'
down_revision = '33aa7aac986c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('human_token', sa.String(length=250), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'human_token')
    # ### end Alembic commands ###
