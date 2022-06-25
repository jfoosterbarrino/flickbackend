"""empty message

Revision ID: 782a1c612af0
Revises: 20ac6a5819df
Create Date: 2022-06-24 20:23:53.223408

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '782a1c612af0'
down_revision = '20ac6a5819df'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_movie',
    sa.Column('movie_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['movie_id'], ['movie.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('movie_id', 'user_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_movie')
    # ### end Alembic commands ###
