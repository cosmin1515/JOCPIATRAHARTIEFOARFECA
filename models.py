from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    games = relationship("Game", back_populates="user")

class Game(Base):
    __tablename__ = "game"
    id = Column(Integer, primary_key=True, index=True)
    score_player = Column(Integer, default=0)
    score_ai = Column(Integer, default=0)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="games")
