"""empty message

Revision ID: 1f1f7014ab11
Revises: 3cf0758d146f
Create Date: 2018-05-08 17:58:03.786020

"""
from alembic import op


# revision identifiers, used by Alembic.
revision = '1f1f7014ab11'
down_revision = '3cf0758d146f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'users', ['email'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='unique')
    # ### end Alembic commands ###
