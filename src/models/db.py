import pyodbc
from models.ticket import Ticket

class Database:
    """
    Simple DB manager for SQL Server.
    """
    def __init__(self, server: str, database: str):
        conn_str = (
            f"DRIVER={{ODBC Driver 18 for SQL Server}};"
            f"SERVER={server};"
            f"DATABASE={database};"
            "Trusted_Connection=yes;"
        )
        self.conn = pyodbc.connect(conn_str)

    def init_schema(self):
        cursor = self.conn.cursor()
        cursor.execute(open('scripts/init_db.sql').read())
        self.conn.commit()

    def save_ticket(self, ticket: Ticket):
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO tickets (title, description, ticket_state, atendimento_state, extra) VALUES (?, ?, ?, ?, ?) ",
            ticket.title,
            ticket.description,
            ticket.ticket_state.name,
            ticket.atendimento_state.name,
            getattr(ticket, 'hardware_type', getattr(ticket, 'module', None))
        )
        self.conn.commit()
        ticket.id = cursor.execute("SELECT @@IDENTITY").fetchval()
        return ticket.id

    def list_tickets(self):
        cursor = self.conn.cursor()
        rows = cursor.execute("SELECT id, title, ticket_state, atendimento_state, extra FROM tickets").fetchall()
        return rows

    def get_ticket(self, ticket_id: int):
        cursor = self.conn.cursor()
        row = cursor.execute(
            "SELECT id, title, description, ticket_state, atendimento_state, extra FROM tickets WHERE id = ?",
            ticket_id
        ).fetchone()
        return row