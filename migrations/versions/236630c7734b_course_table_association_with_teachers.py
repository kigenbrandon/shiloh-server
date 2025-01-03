"""course table association with teachers

Revision ID: 236630c7734b
Revises: d3dacb740b3a
Create Date: 2024-12-29 00:46:47.261220

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '236630c7734b'
down_revision = 'd3dacb740b3a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('teacher_course_association',
    sa.Column('teacher_id', sa.Integer(), nullable=False),
    sa.Column('course_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['course_id'], ['courses.id'], ),
    sa.ForeignKeyConstraint(['teacher_id'], ['teachers.id'], ),
    sa.PrimaryKeyConstraint('teacher_id', 'course_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('teacher_course_association')
    # ### end Alembic commands ###
