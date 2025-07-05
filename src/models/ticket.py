from enum import Enum, auto
from datetime import datetime

class TicketState(Enum):
    porAtender = auto()
    emAtendimento = auto()
    atendido = auto()

class AtendimentoState(Enum):
    aberto = auto()
    resolvido = auto()
    naoResolvido = auto()

class Ticket:
    """
    Base class for ticketes for common fields and state logic
    """
    def __init__(self, title: str, description: str):
        self.id = None  # set by DB
        self.title = title
        self.description = description
        self.created_at = datetime.now()
        self.ticket_state = TicketState.porAtender
        self.atendimento_state = AtendimentoState.aberto

    def can_open(self) -> bool:
        """only tickets that are not atended can be opened"""
        return self.ticket_state != TicketState.atendido

    def open(self):
        if not self.can_open():
            raise ValueError("Ticket já atendido não pode ser reaberto.")
        self.ticket_state = TicketState.emAtendimento

    def close(self, resolved: bool = True):
        self.ticket_state = TicketState.atendido
        self.atendimento_state = AtendimentoState.resolvido if resolved else AtendimentoState.naoResolvido

class HardwareTicket(Ticket):
    """
    Ticket subclass for hardware issues.
    """
    def __init__(self, title: str, description: str, hardware_type: str):
        super().__init__(title, description)
        self.hardware_type = hardware_type

class SoftwareTicket(Ticket):
    """
    Ticket subclass for software issues.
    """
    def __init__(self, title: str, description: str, module: str):
        super().__init__(title, description)
        self.module = module
```

---
