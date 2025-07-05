-- 1)
IF DB_ID(N'ticketApp') IS NULL
BEGIN
    PRINT 'Creating database ticketApp';
    EXEC('CREATE DATABASE ticketApp');
END
GO

-- 2)
USE ticketApp;
GO

-- 3)
IF OBJECT_ID('dbo.tickets', 'U') IS NOT NULL
    DROP TABLE dbo.tickets;
GO

CREATE TABLE dbo.tickets (
    id INT IDENTITY PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    description VARCHAR(MAX),
    creator VARCHAR(100) NOT NULL,
    type VARCHAR(50) NOT NULL,
    subtype VARCHAR(100),
    ticket_state VARCHAR(50) NOT NULL,         -- porAtender, emAtendimento, Atendido
    atendimento_state VARCHAR(50) NOT NULL,     -- aberto, resolvido, naoResolvido
    assigned_to VARCHAR(100),
    attended_at DATETIME,
    technician_notes VARCHAR(MAX)
);
GO

-- 4) (Optional) seed with sample data
-- INSERT INTO dbo.tickets (title, description, creator, type, subtype, ticket_state, atendimento_state)
-- VALUES
-- ('Printer jam','Tray 2 jammed','user1','HardwareTicket','Printer','porAtender','aberto'),
-- ('VPN setup','Need VPN access','user2','SoftwareTicket','VPNModule','porAtender','aberto');
-- GO
