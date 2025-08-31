from datetime import date
from .database import Base, engine, get_session
from .models import User, Goal, Progress

def seed():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    session = get_session()

    user1 = User(name="Roman")
    user2 = User(name="Alice")

    goal1 = Goal(description="Run 5km in under 30 min", target_date=date(2025, 12, 31), user=user1)
    goal2 = Goal(description="Lose 5kg", target_date=date(2025, 11, 30), user=user1)
    goal3 = Goal(description="Do 50 push-ups", target_date=date(2025, 10, 15), user=user2)

    session.add_all([user1, user2, goal1, goal2, goal3])
    session.commit()

    print("Database seeded!")

if __name__ == "__main__":
    seed()