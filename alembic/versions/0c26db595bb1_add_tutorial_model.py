"""Add Tutorial model

Revision ID: 0c26db595bb1
Revises: 
Create Date: 2022-11-20 17:58:20.114120

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "0c26db595bb1"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "app__colleges",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "app__student",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "app__department_batch",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("college_id", sa.Integer(), nullable=True),
        sa.Column("batch", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["college_id"],
            ["app__colleges.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "app__course",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=True),
        sa.Column("department_batch_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["department_batch_id"],
            ["app__department_batch.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "app__student_course",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("course_id", sa.Integer(), nullable=True),
        sa.Column("student_id", sa.Integer(), nullable=True),
        sa.Column("joining_year", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["course_id"],
            ["app__course.id"],
        ),
        sa.ForeignKeyConstraint(
            ["student_id"],
            ["app__student.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("app__student_course")
    op.drop_table("app__course")
    op.drop_table("app__department_batch")
    op.drop_table("app__student")
    op.drop_table("app__colleges")
    # ### end Alembic commands ###
