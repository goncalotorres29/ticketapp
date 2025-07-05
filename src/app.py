import click
from controllers.ticket_controller import TicketController
from models.db import Database

@click.group()
def cli():
    """Console App de Help Desk"""

@cli.command()
def create_db():
    """Cria o schema (tabela tickets) no banco."""
    Database().init_schema()
    click.echo("Schema iniciado (tabela tickets criada).")

@cli.command()
@click.option('--creator',    required=True, help="Usuário que abre o ticket")
@click.option('--type',       'tkt_type', required=True,
              type=click.Choice(['HardwareTicket','SoftwareTicket']),
              help="Tipo de ticket")
@click.option('--subtype',    required=True, help="Subtipo (ex: Printer/Bug)")
@click.option('--title',      required=True, help="Título breve")
@click.option('--description',required=True, help="Descrição detalhada")
def create(creator, tkt_type, subtype, title, description):
    """Abre um novo ticket."""
    TicketController().create(creator, tkt_type, subtype, title, description)

@cli.command()
@click.option('--creator', help="Filtrar apenas tickets de um usuário")
def list(creator):
    """Lista tickets (todos ou de um criador)."""
    TicketController().list(creator)

@cli.command()
@click.argument('ticket_id', type=int)
@click.option('--technician', required=True, help="Técnico que atende")
@click.option('--notes',      required=True, help="Notas do atendimento")
@click.option('--resolved/--unresolved', default=True,
              help="Marcar como resolvido ou não")
def attend(ticket_id, technician, notes, resolved):
    """Atende e fecha um ticket."""
    TicketController().attend(ticket_id, technician, notes, resolved)

if __name__ == '__main__':
    cli()
