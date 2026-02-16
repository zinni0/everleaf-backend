import uuid

from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.core.database import Base

player_positions = Table(
    "player_position",
    Base.metadata,
    Column(
        "player_id",
        UUID(as_uuid=True),
        ForeignKey("players.id", ondelete="CASCADE"),
        primary_key=True,
    ),
    Column(
        "position_id",
        UUID(as_uuid=True),
        ForeignKey("positions.id", ondelete="CASCADE"),
        primary_key=True,
    ),
)


class Players(Base):
    __tablename__ = "players"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    skill_level = Column(Integer, default=1)

    positions = relationship(
        "Position", secondary=player_positions, back_populates="players"
    )
