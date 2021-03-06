"""empty message

Revision ID: 448692da502f
Revises: d44189de519f
Create Date: 2020-05-10 19:15:52.850616

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '448692da502f'
down_revision = 'd44189de519f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('survey_responses', sa.Column('submitted_date', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('survey_responses', 'submitted_date')
    # ### end Alembic commands ###
