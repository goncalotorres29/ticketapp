import click
from controllers.user_controller import UserController

@click.group()
def cli():
    """MyConsoleApp CLI."""
    pass

@cli.command()
@click.argument('name')
def greet(name):
    """Ola utilizador."""
    UserController().greet(name)

if __name__ == '__main__':
    cli()
