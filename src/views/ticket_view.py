class TicketView:
    @staticmethod
    def show_created(ticket_id):
        print(f"[+] Ticket criado com ID: {ticket_id}")

    @staticmethod
    def show_list(rows):
        print("ID | Title               | Creator  | Estado       | Atendimento  ")
        print("---+----------------------+----------+--------------+-------------")
        for r in rows:
            print(f"{r.id:2} | {r.title:20} | {r.creator:8} | "
                  f"{r.ticket_state:12} | {r.atendimento_state}")

    @staticmethod
    def show_attended(ticket_id):
        print(f"[✔] Ticket {ticket_id} atendido e fechado.")

    @staticmethod
    def show_not_found(ticket_id):
        print(f"[!] Ticket {ticket_id} não encontrado.")