from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    goals = relationship("Goal", back_populates="user")

    def __repr__(self):
        return f"<User(id={self.id}, name={self.name})>"

class Goal(Base):
    __tablename__ = "goals"

    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)
    target_date = Column(Date)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="goals")
    progress_entries = relationship("Progress", back_populates="goal")

    def __repr__(self):
        return f"<Goal(id={self.id}, description={self.description})>"

class Progress(Base):
    __tablename__ = "progress"

    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    notes = Column(String)
    goal_id = Column(Integer, ForeignKey("goals.id"))
    goal = relationship("Goal", back_populates="progress_entries")

    def __repr__(self):
        return f"<Progress(id={self.id}, date={self.date})>"
