"""empty message

Revision ID: 6c0937b35c36
Revises: cae90ba45209
Create Date: 2021-08-07 17:54:37.684730

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6c0937b35c36'
down_revision = 'cae90ba45209'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'character', ['id'])
    op.alter_column('user', 'token',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.create_unique_constraint(None, 'user', ['token'])
    op.create_unique_constraint(None, 'user', ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='unique')
    op.drop_constraint(None, 'user', type_='unique')
    op.alter_column('user', 'token',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.drop_constraint(None, 'character', type_='unique')
    # ### end Alembic commands ###
