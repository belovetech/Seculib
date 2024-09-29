"""update the varchar length of all ids

Revision ID: 81f17b10d44b
Revises: 
Create Date: 2024-09-29 13:10:38.565399

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '81f17b10d44b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('borrowed_books', schema=None) as batch_op:
        batch_op.alter_column('book_id',
               existing_type=sa.VARCHAR(length=25),
               type_=sa.String(length=36),
               existing_nullable=True)
        batch_op.alter_column('student_id',
               existing_type=sa.VARCHAR(length=25),
               type_=sa.String(length=36),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('borrowed_books', schema=None) as batch_op:
        batch_op.alter_column('student_id',
               existing_type=sa.String(length=36),
               type_=sa.VARCHAR(length=25),
               existing_nullable=True)
        batch_op.alter_column('book_id',
               existing_type=sa.String(length=36),
               type_=sa.VARCHAR(length=25),
               existing_nullable=True)

    # ### end Alembic commands ###