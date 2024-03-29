"""empty message

Revision ID: 6e0d4f31c035
Revises: 025f5670f8fb
Create Date: 2020-05-10 20:17:32.328546

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6e0d4f31c035'
down_revision = '025f5670f8fb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('survey_responses', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'survey_responses', 'users', ['user_id'], ['user_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'survey_responses', type_='foreignkey')
    op.drop_column('survey_responses', 'user_id')
    # ### end Alembic commands ###
