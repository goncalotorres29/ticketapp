# TicketApp Console

Aplicação de consola em Python para gestão de tickets de help-desk (hardware & software).

**Repositório:** https://github.com/goncalotorres29/ticketapp

---

## Funcionalidades

- **Utilizadores** podem:
  - Criar tickets (hardware ou software)
  - Listar os seus tickets
  - Ver detalhes e estado

- **Técnicos** podem:
  - Listar todos os tickets por atender
  - Atender (atribuir, registar data/hora automática e adicionar notas)
  - Fechar como “resolvido” ou “não resolvido”

- **Tipos de ticket**  
  - **HardwareTicket**: equipamentos, avarias  
  - **SoftwareTicket**: funcionalidades, bugs  

- **Estados**  
  - **Ticket**: porAtender → emAtendimento → Atendido  
  - **Atendimento**: aberto → resolvido / naoResolvido  

---

## Requisitos

- Python 3.7+  
- SQL Server acessível por ODBC  
- Windows/macOS/Linux (com driver ODBC adequado)  

---

## Instalação

1. Clone o repositório  
   ```bash
   git clone https://github.com/goncalotorres29/ticketapp.git
   cd ticketapp
