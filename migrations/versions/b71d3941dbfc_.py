"""empty message

Revision ID: b71d3941dbfc
Revises: 3c276f03bde2
Create Date: 2020-04-19 13:22:37.477065

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'b71d3941dbfc'
down_revision = '3c276f03bde2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('survey_responses', sa.Column('age', sa.String(length=50), nullable=True))
    op.add_column('survey_responses', sa.Column('history_asthma', sa.Boolean(), nullable=True))
    op.add_column('survey_responses', sa.Column('history_bmi_over_40', sa.Boolean(), nullable=True))
    op.add_column('survey_responses', sa.Column('history_cancer', sa.Boolean(), nullable=True))
    op.add_column('survey_responses', sa.Column('history_cardiovascular_disease', sa.Boolean(), nullable=True))
    op.add_column('survey_responses', sa.Column('history_chronic_kidney_disease', sa.Boolean(), nullable=True))
    op.add_column('survey_responses', sa.Column('history_copd_emphysema', sa.Boolean(), nullable=True))
    op.add_column('survey_responses', sa.Column('history_diabetes', sa.Boolean(), nullable=True))
    op.add_column('survey_responses', sa.Column('history_high_blood_pressure', sa.Boolean(), nullable=True))
    op.add_column('survey_responses', sa.Column('history_hiv_aids', sa.Boolean(), nullable=True))
    op.add_column('survey_responses', sa.Column('history_liver_disease', sa.Boolean(), nullable=True))
    op.add_column('survey_responses', sa.Column('household_tested', sa.String(length=50), nullable=True))
    op.add_column('survey_responses', sa.Column('self_tested', sa.String(length=50), nullable=True))
    op.add_column('survey_responses', sa.Column('sex', sa.String(length=2), nullable=True))
    op.add_column('survey_responses', sa.Column('therm_temp', sa.Float(), nullable=True))
    op.drop_column('survey_responses', 'thermometer_temp')
    op.drop_column('survey_responses', 'self_test_result')
    op.drop_column('survey_responses', 'household_test_result')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('survey_responses', sa.Column('household_test_result', mysql.VARCHAR(length=50), nullable=True))
    op.add_column('survey_responses', sa.Column('self_test_result', mysql.VARCHAR(length=50), nullable=True))
    op.add_column('survey_responses', sa.Column('thermometer_temp', mysql.FLOAT(), nullable=True))
    op.drop_column('survey_responses', 'therm_temp')
    op.drop_column('survey_responses', 'sex')
    op.drop_column('survey_responses', 'self_tested')
    op.drop_column('survey_responses', 'household_tested')
    op.drop_column('survey_responses', 'history_liver_disease')
    op.drop_column('survey_responses', 'history_hiv_aids')
    op.drop_column('survey_responses', 'history_high_blood_pressure')
    op.drop_column('survey_responses', 'history_diabetes')
    op.drop_column('survey_responses', 'history_copd_emphysema')
    op.drop_column('survey_responses', 'history_chronic_kidney_disease')
    op.drop_column('survey_responses', 'history_cardiovascular_disease')
    op.drop_column('survey_responses', 'history_cancer')
    op.drop_column('survey_responses', 'history_bmi_over_40')
    op.drop_column('survey_responses', 'history_asthma')
    op.drop_column('survey_responses', 'age')
    # ### end Alembic commands ###
