from models.db import Database
from models.ticket import HardwareTicket, SoftwareTicket, Ticket
from views.ticket_view import TicketView

class TicketController:
    def __init__(self):
        self.db = Database()

    def create(self, creator, tkt_type, subtype, title, description):
        cls = HardwareTicket if tkt_type=='HardwareTicket' else SoftwareTicket
        ticket = cls(title, description, creator, subtype)
        tid = self.db.save_ticket(ticket)
        TicketView.show_created(tid)

    def list(self, creator=None):
        rows = self.db.list_tickets(creator)
        TicketView.show_list(rows)

    def attend(self, ticket_id, technician, notes, resolved):
        row = self.db.get_ticket(ticket_id)
        if not row:
            return TicketView.show_not_found(ticket_id)

        # rehydrate
        _, title, desc, creator, ttype, subtype, *_ , assigned, att_at, tech_notes = row
        cls = HardwareTicket if ttype=='HardwareTicket' else SoftwareTicket
        ticket = cls(title, desc, creator, subtype)
        ticket.id = ticket_id
        ticket.ticket_state = Ticket.State[row.ticket_state]
        ticket.atendimento_state = Ticket.AtendimentoState[row.atendimento_state]

        ticket.open(technician)
        ticket.close(resolved, notes)
        self.db.update_ticket(ticket)
        TicketView.show_attended(ticket_id)