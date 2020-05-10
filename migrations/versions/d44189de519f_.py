"""empty message

Revision ID: d44189de519f
Revises: 4d94dfdc04c1
Create Date: 2020-05-10 19:11:11.753378

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'd44189de519f'
down_revision = '4d94dfdc04c1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('survey_responses', sa.Column('chest_pain', sa.Boolean(), nullable=True))
    op.add_column('survey_responses', sa.Column('headache', sa.Boolean(), nullable=True))
    op.add_column('survey_responses', sa.Column('loss_of_smell', sa.Boolean(), nullable=True))
    op.add_column('survey_responses', sa.Column('loss_of_taste', sa.Boolean(), nullable=True))
    op.add_column('survey_responses', sa.Column('nausea', sa.Boolean(), nullable=True))
    op.add_column('survey_responses', sa.Column('rash_on_feet', sa.Boolean(), nullable=True))
    op.add_column('survey_responses', sa.Column('tightness_chest', sa.Boolean(), nullable=True))
    op.add_column('survey_responses', sa.Column('vomiting', sa.Boolean(), nullable=True))
    op.alter_column('survey_responses', 'age',
               existing_type=mysql.VARCHAR(length=50),
               type_=sa.Integer(),
               existing_nullable=True)
    op.drop_column('survey_responses', 'pressure_chest')
    op.drop_column('survey_responses', 'submitted')
    op.drop_column('survey_responses', 'feeling_well')
    op.drop_column('survey_responses', 'no_smell_taste')
    op.drop_column('survey_responses', 'nausea_vomiting')
    op.drop_column('survey_responses', 'pink_eye')
    op.drop_column('survey_responses', 'sentiment')
    op.drop_column('users', 'date_join')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('date_join', mysql.DATETIME(), nullable=True))
    op.add_column('survey_responses', sa.Column('sentiment', mysql.VARCHAR(length=250), nullable=True))
    op.add_column('survey_responses', sa.Column('pink_eye', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True))
    op.add_column('survey_responses', sa.Column('nausea_vomiting', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True))
    op.add_column('survey_responses', sa.Column('no_smell_taste', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True))
    op.add_column('survey_responses', sa.Column('feeling_well', mysql.VARCHAR(length=50), nullable=True))
    op.add_column('survey_responses', sa.Column('submitted', mysql.DATETIME(), nullable=True))
    op.add_column('survey_responses', sa.Column('pressure_chest', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True))
    op.alter_column('survey_responses', 'age',
               existing_type=sa.Integer(),
               type_=mysql.VARCHAR(length=50),
               existing_nullable=True)
    op.drop_column('survey_responses', 'vomiting')
    op.drop_column('survey_responses', 'tightness_chest')
    op.drop_column('survey_responses', 'rash_on_feet')
    op.drop_column('survey_responses', 'nausea')
    op.drop_column('survey_responses', 'loss_of_taste')
    op.drop_column('survey_responses', 'loss_of_smell')
    op.drop_column('survey_responses', 'headache')
    op.drop_column('survey_responses', 'chest_pain')
    # ### end Alembic commands ###