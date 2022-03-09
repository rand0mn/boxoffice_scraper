"""Create tables: movies, weekends, weekly_box_offices.

Revision ID: 9483fe5c4386
Revises: 
Create Date: 2022-03-03 11:14:44.171471

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9483fe5c4386'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('movies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('origin_name', sa.String(), nullable=True),
    sa.Column('year', sa.SmallInteger(), nullable=False),
    sa.Column('countries', sa.String(), nullable=True),
    sa.Column('genres', sa.String(), nullable=True),
    sa.Column('certificate', sa.String(), nullable=True),
    sa.Column('mpaa', sa.String(), nullable=True),
    sa.Column('duration', sa.String(), nullable=True),
    sa.Column('director', sa.String(), nullable=True),
    sa.Column('writer', sa.String(), nullable=True),
    sa.Column('producer', sa.String(), nullable=True),
    sa.Column('operator', sa.String(), nullable=True),
    sa.Column('composer', sa.String(), nullable=True),
    sa.Column('design', sa.String(), nullable=True),
    sa.Column('editor', sa.String(), nullable=True),
    sa.Column('actor', sa.String(), nullable=True),
    sa.Column('user_score', sa.String(), nullable=True),
    sa.Column('critic_score', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('weekends',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date_range', sa.String(length=30), nullable=False),
    sa.Column('date_start', sa.Date(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('date_start')
    )
    op.create_table('weekly_box_offices',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('weekend_gross', sa.Integer(), nullable=True),
    sa.Column('weekend_session_gross', sa.Integer(), nullable=True),
    sa.Column('gross', sa.BigInteger(), nullable=True),
    sa.Column('session_gross', sa.Integer(), nullable=True),
    sa.Column('weekend_viewers', sa.Integer(), nullable=True),
    sa.Column('viewers', sa.BigInteger(), nullable=True),
    sa.Column('n_copies', sa.SmallInteger(), nullable=True),
    sa.Column('n_weekends', sa.SmallInteger(), nullable=True),
    sa.Column('distributor', sa.String(), nullable=True),
    sa.Column('movie_ref', sa.Integer(), nullable=False),
    sa.Column('weekend', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('weekly_box_offices')
    op.drop_table('weekends')
    op.drop_table('movies')
    # ### end Alembic commands ###
