"""Update models

Revision ID: 32de6a6269f5
Revises: 
Create Date: 2024-08-03 10:54:36.093301

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '32de6a6269f5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('student')
    op.drop_table('book')
    op.drop_table('session')
    op.drop_table('borrowed_book')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('borrowed_book',
    sa.Column('id', sa.VARCHAR(length=25), nullable=False),
    sa.Column('book_id', sa.VARCHAR(length=25), nullable=True),
    sa.Column('student_id', sa.VARCHAR(length=25), nullable=True),
    sa.Column('borrow_date', sa.DATETIME(), nullable=True),
    sa.Column('return_date', sa.DATETIME(), nullable=True),
    sa.ForeignKeyConstraint(['book_id'], ['book.id'], ),
    sa.ForeignKeyConstraint(['student_id'], ['student.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('session',
    sa.Column('id', sa.VARCHAR(length=25), nullable=False),
    sa.Column('student_id', sa.VARCHAR(length=25), nullable=True),
    sa.Column('created_at', sa.DATETIME(), nullable=True),
    sa.Column('expiry_at', sa.DATETIME(), nullable=True),
    sa.ForeignKeyConstraint(['student_id'], ['student.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('book',
    sa.Column('id', sa.VARCHAR(length=25), nullable=False),
    sa.Column('title', sa.VARCHAR(length=200), nullable=False),
    sa.Column('author', sa.VARCHAR(length=100), nullable=False),
    sa.Column('available', sa.BOOLEAN(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('student',
    sa.Column('id', sa.VARCHAR(length=25), nullable=False),
    sa.Column('name', sa.VARCHAR(length=100), nullable=False),
    sa.Column('email', sa.VARCHAR(length=120), nullable=False),
    sa.Column('matric_no', sa.VARCHAR(length=20), nullable=False),
    sa.Column('department', sa.VARCHAR(length=55), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('matric_no')
    )
    # ### end Alembic commands ###