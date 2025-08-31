import click
from datetime import datetime
from .database import get_session, Base, engine
from .models import User, Goal, Progress

@click.group()
def cli():
    """Fitness Goal Tracker CLI"""
    pass

@cli.command()
@click.argument("name")
def add_user(name):
    """Add a new user"""
    session = get_session()
    user = User(name=name)
    session.add(user)
    session.commit()
    click.echo(f"User '{name}' added with ID {user.id}")

@cli.command()
def list_users():
    """List all users"""
    session = get_session()
    users = session.query(User).all()
    for u in users:
        click.echo(f"{u.id}: {u.name}")

@cli.command()
@click.argument("user_id", type=int)
@click.argument("description")
@click.argument("target_date")
def add_goal(user_id, description, target_date):
    """Add a fitness goal for a user (date format: YYYY-MM-DD)"""
    session = get_session()
    user = session.query(User).get(user_id)
    if not user:
        click.echo("User not found")
        return
    goal = Goal(description=description, target_date=datetime.strptime(target_date, "%Y-%m-%d"), user=user)
    session.add(goal)
    session.commit()
    click.echo(f"Goal '{description}' added for {user.name}")

@cli.command()
@click.argument("goal_id", type=int)
@click.argument("notes")
def add_progress(goal_id, notes):
    """Log progress for a goal"""
    session = get_session()
    goal = session.query(Goal).get(goal_id)
    if not goal:
        click.echo("Goal not found")
        return
    progress = Progress(date=datetime.today(), notes=notes, goal=goal)
    session.add(progress)
    session.commit()
    click.echo(f"Progress logged for goal '{goal.description}'")

@cli.command()
@click.argument("user_id", type=int)
def show_goals(user_id):
    """Show all goals for a user"""
    session = get_session()
    user = session.query(User).get(user_id)
    if not user:
        click.echo("User not found")
        return
    for g in user.goals:
        click.echo(f" {g.description} (target: {g.target_date})")

if __name__ == "__main__":
    Base.metadata.create_all(engine)  # Ensure tables exist
    cli()
