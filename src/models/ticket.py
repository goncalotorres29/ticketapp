rom enum import Enum
from datetime import datetime

class Ticket:
    class State(Enum):
        porAtender = 1
        emAtendimento = 2
        Atendido = 3

    class AtendimentoState(Enum):
        aberto = 1
        resolvido = 2
        naoResolvido = 3

    def __init__(self, title, description, creator, subtype):
        self.id = None
        self.title = title
        self.description = description
        self.creator = creator
        self.subtype = subtype
        self.ticket_state = Ticket.State.porAtender
        self.atendimento_state = Ticket.AtendimentoState.aberto
        self.assigned_to = None
        self.attended_at = None
        self.technician_notes = None

    def open(self, technician):
        if self.ticket_state != Ticket.State.porAtender:
            raise ValueError("Ticket já foi atendido ou está em atendimento.")
        self.assigned_to = technician
        self.ticket_state = Ticket.State.emAtendimento
        self.attended_at = datetime.now()

    def close(self, resolved: bool, notes: str):
        if self.ticket_state != Ticket.State.emAtendimento:
            raise ValueError("Ticket não está em atendimento.")
        self.ticket_state = Ticket.State.Atendido
        self.atendimento_state = (Ticket.AtendimentoState.resolvido
                                  if resolved
                                  else Ticket.AtendimentoState.naoResolvido)
        self.technician_notes = notes

class HardwareTicket(Ticket):
    """
    Para tickets de hardware (equipamento, avaria).
    """
    def __init__(self, title, description, creator, subtype):
        super().__init__(title, description, creator, subtype)

class SoftwareTicket(Ticket):
    """
    Para tickets de software (descrição de necessidade).
    """
    def __init__(self, title, description, creator, subtype):
        super().__init__(title, description, creator, subtype)