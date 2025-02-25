"""ref_user_and_profile_link

Revision ID: b5dc43e9a0cc
Revises: 264cebfba456
Create Date: 2025-02-25 22:42:22.981479

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "b5dc43e9a0cc"
down_revision: Union[str, None] = "264cebfba456"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "profile", sa.Column("user_id", sa.Integer(), nullable=False)
    )
    op.create_unique_constraint(None, "profile", ["user_id"])
    op.create_foreign_key(None, "profile", "user", ["user_id"], ["id"])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "profile", type_="foreignkey")
    op.drop_constraint(None, "profile", type_="unique")
    op.drop_column("profile", "user_id")
    # ### end Alembic commands ###
