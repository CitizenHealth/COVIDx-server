"""empty message

Revision ID: f3e4da3a3639
Revises: dee157fbd76d
Create Date: 2020-05-10 16:45:38.476688

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'f3e4da3a3639'
down_revision = 'dee157fbd76d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('test_status_id', table_name='test_status')
    op.drop_table('test_status')
    op.drop_index('symptom_id', table_name='symptom')
    op.drop_table('symptom')
    op.drop_index('survey_id', table_name='survey_metadata')
    op.drop_table('survey_metadata')
    op.drop_index('sentiment_id', table_name='sentiment')
    op.drop_table('sentiment')
    op.drop_index('temperature_id', table_name='temperature')
    op.drop_table('temperature')
    op.drop_index('location_id', table_name='location')
    op.drop_table('location')
    op.drop_index('medical_history_id', table_name='medical_history')
    op.drop_table('medical_history')
    op.alter_column('roles', 'role_id',
               existing_type=mysql.VARCHAR(length=50),
               type_=sa.Integer(),
               autoincrement=True)
    op.add_column('users', sa.Column('role_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'users', 'roles', ['role_id'], ['role_id'])
    op.drop_column('users', 'is_staff')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('is_staff', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.drop_column('users', 'role_id')
    op.alter_column('roles', 'role_id',
               existing_type=sa.Integer(),
               type_=mysql.VARCHAR(length=50),
               autoincrement=True)
    op.create_table('medical_history',
    sa.Column('medical_history_id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('survey_id', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('high_blood_pressure', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True),
    sa.Column('asthma', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True),
    sa.Column('copd_emphysema', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True),
    sa.Column('chronic_kidney_disease', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True),
    sa.Column('liver_disease', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True),
    sa.Column('cancer', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True),
    sa.Column('diabetes', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True),
    sa.Column('cardiovascular_disease', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True),
    sa.Column('hiv_aids', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True),
    sa.Column('bmi_over_40', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True),
    sa.CheckConstraint('(`asthma` in (0,1))', name='medical_history_chk_2'),
    sa.CheckConstraint('(`bmi_over_40` in (0,1))', name='medical_history_chk_10'),
    sa.CheckConstraint('(`cancer` in (0,1))', name='medical_history_chk_6'),
    sa.CheckConstraint('(`cardiovascular_disease` in (0,1))', name='medical_history_chk_8'),
    sa.CheckConstraint('(`chronic_kidney_disease` in (0,1))', name='medical_history_chk_4'),
    sa.CheckConstraint('(`copd_emphysema` in (0,1))', name='medical_history_chk_3'),
    sa.CheckConstraint('(`diabetes` in (0,1))', name='medical_history_chk_7'),
    sa.CheckConstraint('(`high_blood_pressure` in (0,1))', name='medical_history_chk_1'),
    sa.CheckConstraint('(`hiv_aids` in (0,1))', name='medical_history_chk_9'),
    sa.CheckConstraint('(`liver_disease` in (0,1))', name='medical_history_chk_5'),
    sa.ForeignKeyConstraint(['survey_id'], ['survey_metadata.survey_id'], name='medical_history_ibfk_1'),
    sa.PrimaryKeyConstraint('medical_history_id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('medical_history_id', 'medical_history', ['medical_history_id'], unique=True)
    op.create_table('location',
    sa.Column('location_id', mysql.VARCHAR(length=50), nullable=False),
    sa.Column('survey_id', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('latitude', mysql.FLOAT(), nullable=True),
    sa.Column('longitude', mysql.FLOAT(), nullable=True),
    sa.Column('date', mysql.DATETIME(), nullable=True),
    sa.Column('zip_code', mysql.VARCHAR(length=25), nullable=True),
    sa.ForeignKeyConstraint(['survey_id'], ['survey_metadata.survey_id'], name='location_ibfk_1'),
    sa.PrimaryKeyConstraint('location_id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('location_id', 'location', ['location_id'], unique=True)
    op.create_table('temperature',
    sa.Column('temperature_id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('survey_id', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('therm_temp', mysql.FLOAT(), nullable=True),
    sa.Column('temp_guess', mysql.VARCHAR(length=50), nullable=True),
    sa.ForeignKeyConstraint(['survey_id'], ['survey_metadata.survey_id'], name='temperature_ibfk_1'),
    sa.PrimaryKeyConstraint('temperature_id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('temperature_id', 'temperature', ['temperature_id'], unique=True)
    op.create_table('sentiment',
    sa.Column('sentiment_id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('survey_id', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('sentiment', mysql.VARCHAR(length=250), nullable=True),
    sa.ForeignKeyConstraint(['survey_id'], ['survey_metadata.survey_id'], name='sentiment_ibfk_1'),
    sa.PrimaryKeyConstraint('sentiment_id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('sentiment_id', 'sentiment', ['sentiment_id'], unique=True)
    op.create_table('survey_metadata',
    sa.Column('survey_id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_id', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('datetime_submitted', mysql.DATETIME(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], name='survey_metadata_ibfk_1'),
    sa.PrimaryKeyConstraint('survey_id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('survey_id', 'survey_metadata', ['survey_id'], unique=True)
    op.create_table('symptom',
    sa.Column('symptom_id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('survey_id', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('no_smell_taste', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True),
    sa.Column('extreme_fatigue', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True),
    sa.Column('wet_cough', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True),
    sa.Column('dry_cough', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True),
    sa.Column('abdominal_pain', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True),
    sa.Column('diarrhea', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True),
    sa.Column('sore_throat', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True),
    sa.Column('chills', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True),
    sa.Column('nausea_vomiting', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True),
    sa.Column('pressure_chest', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True),
    sa.Column('pink_eye', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True),
    sa.Column('other', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True),
    sa.Column('feeling_well', mysql.VARCHAR(length=50), nullable=True),
    sa.CheckConstraint('(`abdominal_pain` in (0,1))', name='symptom_chk_5'),
    sa.CheckConstraint('(`chills` in (0,1))', name='symptom_chk_8'),
    sa.CheckConstraint('(`diarrhea` in (0,1))', name='symptom_chk_6'),
    sa.CheckConstraint('(`dry_cough` in (0,1))', name='symptom_chk_4'),
    sa.CheckConstraint('(`extreme_fatigue` in (0,1))', name='symptom_chk_2'),
    sa.CheckConstraint('(`nausea_vomiting` in (0,1))', name='symptom_chk_9'),
    sa.CheckConstraint('(`no_smell_taste` in (0,1))', name='symptom_chk_1'),
    sa.CheckConstraint('(`other` in (0,1))', name='symptom_chk_12'),
    sa.CheckConstraint('(`pink_eye` in (0,1))', name='symptom_chk_11'),
    sa.CheckConstraint('(`pressure_chest` in (0,1))', name='symptom_chk_10'),
    sa.CheckConstraint('(`sore_throat` in (0,1))', name='symptom_chk_7'),
    sa.CheckConstraint('(`wet_cough` in (0,1))', name='symptom_chk_3'),
    sa.ForeignKeyConstraint(['survey_id'], ['survey_metadata.survey_id'], name='symptom_ibfk_1'),
    sa.PrimaryKeyConstraint('symptom_id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('symptom_id', 'symptom', ['symptom_id'], unique=True)
    op.create_table('test_status',
    sa.Column('test_status_id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('survey_id', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('self_tested', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('self_tested_date', mysql.DATETIME(), nullable=True),
    sa.Column('household_tested', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('household_tested_date', mysql.DATETIME(), nullable=True),
    sa.ForeignKeyConstraint(['survey_id'], ['survey_metadata.survey_id'], name='test_status_ibfk_1'),
    sa.PrimaryKeyConstraint('test_status_id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('test_status_id', 'test_status', ['test_status_id'], unique=True)
    # ### end Alembic commands ###