import uuid

from sqlalchemy import UUID, Column, String
from sqlalchemy.orm import relationship

from app.core.database import Base
from app.models.player import player_positions


class Position(Base):
    __tablename__ = "positions"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False, unique=True)

    players = relationship(
        "Player", secondary=player_positions, back_populates="positions"
    )
