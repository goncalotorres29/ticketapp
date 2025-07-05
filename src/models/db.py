# src/models/db.py
import pyodbc
from datetime import datetime

class Database:
    """
    Wraps pyodbc connection and provides methods for tickets.
    """
    def __init__(self,
                 server: str = 'localhost\\SQLEXPRESS',
                 database: str = 'ticketApp'):
        self.conn_str = (
            'DRIVER={ODBC Driver 18 for SQL Server};'
            f'SERVER={server};'
            f'DATABASE={database};'
            'Trusted_Connection=yes;'
        )

    def connect(self):
        return pyodbc.connect(self.conn_str)

    def init_schema(self):
        with self.connect() as conn:
            cur = conn.cursor()
            cur.execute("""
                IF OBJECT_ID('dbo.tickets','U') IS NULL
                CREATE TABLE dbo.tickets (
                    id INT IDENTITY PRIMARY KEY,
                    title VARCHAR(200) NOT NULL,
                    description VARCHAR(MAX),
                    creator VARCHAR(100) NOT NULL,
                    type VARCHAR(50) NOT NULL,
                    subtype VARCHAR(100),
                    ticket_state VARCHAR(50) NOT NULL,
                    atendimento_state VARCHAR(50) NOT NULL,
                    assigned_to VARCHAR(100),
                    attended_at DATETIME,
                    technician_notes VARCHAR(MAX)
                )
            """)
            conn.commit()

    def save_ticket(self, ticket):
        with self.connect() as conn:
            cur = conn.cursor()
            cur.execute("""
                INSERT INTO dbo.tickets
                  (title, description, creator, type, subtype, ticket_state, atendimento_state)
                VALUES (?,?,?,?,?,?,?)
            """, ticket.title, ticket.description, ticket.creator,
                 ticket.__class__.__name__, ticket.subtype,
                 ticket.ticket_state.name, ticket.atendimento_state.name)
            conn.commit()
            return cur.execute("SELECT @@IDENTITY").fetchval()

    def list_tickets(self, creator=None):
        with self.connect() as conn:
            cur = conn.cursor()
            if creator:
                cur.execute("SELECT * FROM dbo.tickets WHERE creator=?", creator)
            else:
                cur.execute("SELECT * FROM dbo.tickets")
            return cur.fetchall()

    def get_ticket(self, ticket_id):
        with self.connect() as conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM dbo.tickets WHERE id=?", ticket_id)
            return cur.fetchone()

    def update_ticket(self, ticket):
        with self.connect() as conn:
            cur = conn.cursor()
            cur.execute("""
                UPDATE dbo.tickets
                SET ticket_state=?, atendimento_state=?,
                    assigned_to=?, attended_at=?, technician_notes=?
                WHERE id=?
            """, ticket.ticket_state.name, ticket.atendimento_state.name,
                 ticket.assigned_to, ticket.attended_at, ticket.technician_notes,
                 ticket.id)
            conn.commit()
