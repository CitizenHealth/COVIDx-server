"""empty message

Revision ID: 2d9b98790d8c
Revises: 448692da502f
Create Date: 2020-05-10 20:06:44.404008

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '2d9b98790d8c'
down_revision = '448692da502f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('hash', table_name='state_results')
    op.drop_table('state_results')
    op.drop_index('ix_roles_description', table_name='roles')
    op.drop_index('ix_roles_name', table_name='roles')
    op.drop_index('role_id', table_name='roles')
    op.drop_table('roles')
    op.drop_index('location_id', table_name='location')
    op.drop_table('location')
    op.add_column('survey_responses', sa.Column('abdominal_pain', sa.Boolean(), nullable=True))
    op.add_column('survey_responses', sa.Column('asthma', sa.Boolean(), nullable=True))
    op.add_column('survey_responses', sa.Column('bmi_over_40', sa.Boolean(), nullable=True))
    op.add_column('survey_responses', sa.Column('cancer', sa.Boolean(), nullable=True))
    op.add_column('survey_responses', sa.Column('cardiovascular_disease', sa.Boolean(), nullable=True))
    op.add_column('survey_responses', sa.Column('chest_pain', sa.Boolean(), nullable=True))
    op.add_column('survey_responses', sa.Column('chills', sa.Boolean(), nullable=True))
    op.add_column('survey_responses', sa.Column('chronic_kidney_disease', sa.Boolean(), nullable=True))
    op.add_column('survey_responses', sa.Column('copd_emphysema', sa.Boolean(), nullable=True))
    op.add_column('survey_responses', sa.Column('diabetes', sa.Boolean(), nullable=True))
    op.add_column('survey_responses', sa.Column('diarrhea', sa.Boolean(), nullable=True))
    op.add_column('survey_responses', sa.Column('dry_cough', sa.Boolean(), nullable=True))
    op.add_column('survey_responses', sa.Column('extreme_fatigue', sa.Boolean(), nullable=True))
    op.add_column('survey_responses', sa.Column('headache', sa.Boolean(), nullable=True))
    op.add_column('survey_responses', sa.Column('high_blood_pressure', sa.Boolean(), nullable=True))
    op.add_column('survey_responses', sa.Column('hiv_aids', sa.Boolean(), nullable=True))
    op.add_column('survey_responses', sa.Column('liver_disease', sa.Boolean(), nullable=True))
    op.add_column('survey_responses', sa.Column('loss_of_smell', sa.Boolean(), nullable=True))
    op.add_column('survey_responses', sa.Column('loss_of_taste', sa.Boolean(), nullable=True))
    op.add_column('survey_responses', sa.Column('nausea', sa.Boolean(), nullable=True))
    op.add_column('survey_responses', sa.Column('other', sa.Boolean(), nullable=True))
    op.add_column('survey_responses', sa.Column('rash_on_feet', sa.Boolean(), nullable=True))
    op.add_column('survey_responses', sa.Column('sore_throat', sa.Boolean(), nullable=True))
    op.add_column('survey_responses', sa.Column('submitted_date', sa.DateTime(), nullable=True))
    op.add_column('survey_responses', sa.Column('tightness_chest', sa.Boolean(), nullable=True))
    op.add_column('survey_responses', sa.Column('vomiting', sa.Boolean(), nullable=True))
    op.add_column('survey_responses', sa.Column('wet_cough', sa.Boolean(), nullable=True))
    op.alter_column('survey_responses', 'age',
               existing_type=mysql.VARCHAR(length=50),
               type_=sa.Integer(),
               existing_nullable=True)
    op.alter_column('survey_responses', 'user_id',
               existing_type=mysql.VARCHAR(length=50),
               type_=sa.Integer(),
               existing_nullable=True)
    op.drop_column('survey_responses', 'has_symptom_no_smell_taste')
    op.drop_column('survey_responses', 'has_symptom_pressure_chest')
    op.drop_column('survey_responses', 'history_diabetes')
    op.drop_column('survey_responses', 'has_symptom_pink_eye')
    op.drop_column('survey_responses', 'feeling_well')
    op.drop_column('survey_responses', 'has_symptom_extreme_fatigue')
    op.drop_column('survey_responses', 'has_symptom_nausea_vomiting')
    op.drop_column('survey_responses', 'has_symptom_sore_throat')
    op.drop_column('survey_responses', 'history_cancer')
    op.drop_column('survey_responses', 'has_symptom_diarrhea')
    op.drop_column('survey_responses', 'history_liver_disease')
    op.drop_column('survey_responses', 'has_symptom_dry_cough')
    op.drop_column('survey_responses', 'has_symptom_abdominal_pain')
    op.drop_column('survey_responses', 'history_bmi_over_40')
    op.drop_column('survey_responses', 'history_asthma')
    op.drop_column('survey_responses', 'datetime_submitted')
    op.drop_column('survey_responses', 'history_chronic_kidney_disease')
    op.drop_column('survey_responses', 'history_copd_emphysema')
    op.drop_column('survey_responses', 'has_symptom_other')
    op.drop_column('survey_responses', 'history_cardiovascular_disease')
    op.drop_column('survey_responses', 'has_symptom_wet_cough')
    op.drop_column('survey_responses', 'history_hiv_aids')
    op.drop_column('survey_responses', 'history_high_blood_pressure')
    op.drop_column('survey_responses', 'has_symptom_chills')
    op.add_column('users', sa.Column('date_birth', sa.DateTime(), nullable=True))
    op.add_column('users', sa.Column('firebase_id', sa.String(length=50), nullable=False))
    op.add_column('users', sa.Column('sex', sa.String(length=2), nullable=True))
    op.alter_column('users', 'user_id',
               existing_type=mysql.VARCHAR(length=50),
               type_=sa.Integer(),
               autoincrement=True)
    op.create_unique_constraint(None, 'users', ['firebase_id'])
    op.drop_column('users', 'img_link')
    op.drop_column('users', 'is_staff')
    op.drop_column('users', 'zip_code')
    op.drop_column('users', 'email')
    op.drop_column('users', 'human_token')
    op.drop_column('users', 'display_name')
    op.drop_column('users', 'access_token')
    op.drop_column('users', 'date_join')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('date_join', mysql.DATETIME(), nullable=True))
    op.add_column('users', sa.Column('access_token', mysql.VARCHAR(length=250), nullable=True))
    op.add_column('users', sa.Column('display_name', mysql.VARCHAR(length=50), nullable=True))
    op.add_column('users', sa.Column('human_token', mysql.VARCHAR(length=250), nullable=True))
    op.add_column('users', sa.Column('email', mysql.VARCHAR(length=50), nullable=True))
    op.add_column('users', sa.Column('zip_code', mysql.VARCHAR(length=10), nullable=True))
    op.add_column('users', sa.Column('is_staff', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True))
    op.add_column('users', sa.Column('img_link', mysql.VARCHAR(length=250), nullable=True))
    op.drop_constraint(None, 'users', type_='unique')
    op.alter_column('users', 'user_id',
               existing_type=sa.Integer(),
               type_=mysql.VARCHAR(length=50),
               autoincrement=True)
    op.drop_column('users', 'sex')
    op.drop_column('users', 'firebase_id')
    op.drop_column('users', 'date_birth')
    op.add_column('survey_responses', sa.Column('has_symptom_chills', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True))
    op.add_column('survey_responses', sa.Column('history_high_blood_pressure', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True))
    op.add_column('survey_responses', sa.Column('history_hiv_aids', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True))
    op.add_column('survey_responses', sa.Column('has_symptom_wet_cough', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True))
    op.add_column('survey_responses', sa.Column('history_cardiovascular_disease', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True))
    op.add_column('survey_responses', sa.Column('has_symptom_other', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True))
    op.add_column('survey_responses', sa.Column('history_copd_emphysema', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True))
    op.add_column('survey_responses', sa.Column('history_chronic_kidney_disease', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True))
    op.add_column('survey_responses', sa.Column('datetime_submitted', mysql.DATETIME(), nullable=True))
    op.add_column('survey_responses', sa.Column('history_asthma', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True))
    op.add_column('survey_responses', sa.Column('history_bmi_over_40', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True))
    op.add_column('survey_responses', sa.Column('has_symptom_abdominal_pain', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True))
    op.add_column('survey_responses', sa.Column('has_symptom_dry_cough', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True))
    op.add_column('survey_responses', sa.Column('history_liver_disease', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True))
    op.add_column('survey_responses', sa.Column('has_symptom_diarrhea', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True))
    op.add_column('survey_responses', sa.Column('history_cancer', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True))
    op.add_column('survey_responses', sa.Column('has_symptom_sore_throat', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True))
    op.add_column('survey_responses', sa.Column('has_symptom_nausea_vomiting', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True))
    op.add_column('survey_responses', sa.Column('has_symptom_extreme_fatigue', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True))
    op.add_column('survey_responses', sa.Column('feeling_well', mysql.VARCHAR(length=50), nullable=True))
    op.add_column('survey_responses', sa.Column('has_symptom_pink_eye', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True))
    op.add_column('survey_responses', sa.Column('history_diabetes', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True))
    op.add_column('survey_responses', sa.Column('has_symptom_pressure_chest', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True))
    op.add_column('survey_responses', sa.Column('has_symptom_no_smell_taste', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True))
    op.alter_column('survey_responses', 'user_id',
               existing_type=sa.Integer(),
               type_=mysql.VARCHAR(length=50),
               existing_nullable=True)
    op.alter_column('survey_responses', 'age',
               existing_type=sa.Integer(),
               type_=mysql.VARCHAR(length=50),
               existing_nullable=True)
    op.drop_column('survey_responses', 'wet_cough')
    op.drop_column('survey_responses', 'vomiting')
    op.drop_column('survey_responses', 'tightness_chest')
    op.drop_column('survey_responses', 'submitted_date')
    op.drop_column('survey_responses', 'sore_throat')
    op.drop_column('survey_responses', 'rash_on_feet')
    op.drop_column('survey_responses', 'other')
    op.drop_column('survey_responses', 'nausea')
    op.drop_column('survey_responses', 'loss_of_taste')
    op.drop_column('survey_responses', 'loss_of_smell')
    op.drop_column('survey_responses', 'liver_disease')
    op.drop_column('survey_responses', 'hiv_aids')
    op.drop_column('survey_responses', 'high_blood_pressure')
    op.drop_column('survey_responses', 'headache')
    op.drop_column('survey_responses', 'extreme_fatigue')
    op.drop_column('survey_responses', 'dry_cough')
    op.drop_column('survey_responses', 'diarrhea')
    op.drop_column('survey_responses', 'diabetes')
    op.drop_column('survey_responses', 'copd_emphysema')
    op.drop_column('survey_responses', 'chronic_kidney_disease')
    op.drop_column('survey_responses', 'chills')
    op.drop_column('survey_responses', 'chest_pain')
    op.drop_column('survey_responses', 'cardiovascular_disease')
    op.drop_column('survey_responses', 'cancer')
    op.drop_column('survey_responses', 'bmi_over_40')
    op.drop_column('survey_responses', 'asthma')
    op.drop_column('survey_responses', 'abdominal_pain')
    op.create_table('location',
    sa.Column('location_id', mysql.VARCHAR(length=50), nullable=False),
    sa.Column('user_id', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('lat', mysql.FLOAT(), nullable=True),
    sa.Column('lon', mysql.FLOAT(), nullable=True),
    sa.Column('date', mysql.DATETIME(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], name='location_ibfk_1'),
    sa.PrimaryKeyConstraint('location_id'),
    mysql_default_charset='latin1',
    mysql_engine='InnoDB'
    )
    op.create_index('location_id', 'location', ['location_id'], unique=True)
    op.create_table('roles',
    sa.Column('name', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('description', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('role_id', mysql.VARCHAR(length=50), nullable=False),
    mysql_default_charset='latin1',
    mysql_engine='InnoDB'
    )
    op.create_index('role_id', 'roles', ['role_id'], unique=True)
    op.create_index('ix_roles_name', 'roles', ['name'], unique=False)
    op.create_index('ix_roles_description', 'roles', ['description'], unique=False)
    op.create_table('state_results',
    sa.Column('state', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('positive', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('positiveScore', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('negativeScore', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('negativeRegularScore', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('commercialScore', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('grade', mysql.VARCHAR(length=5), nullable=True),
    sa.Column('score', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('negative', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('pending', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('hospitalizedCurrently', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('hospitalizedCumulative', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('inIcuCurrently', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('inIcuCumulative', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('onVentilatorCurrently', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('onVentilatorCumulative', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('recovered', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('lastUpdateEt', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('checkTimeEt', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('death', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('hospitalized', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('total', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('totalTestResults', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('posNeg', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('fips', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('dateModified', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('dateChecked', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('notes', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('hash', mysql.VARCHAR(length=50), nullable=False),
    sa.Column('latitude', mysql.FLOAT(), nullable=True),
    sa.Column('longitude', mysql.FLOAT(), nullable=True),
    sa.PrimaryKeyConstraint('hash'),
    mysql_default_charset='latin1',
    mysql_engine='InnoDB'
    )
    op.create_index('hash', 'state_results', ['hash'], unique=True)
    # ### end Alembic commands ###
