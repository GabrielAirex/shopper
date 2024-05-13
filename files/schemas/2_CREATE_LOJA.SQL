CREATE TABLE public.Lojas (
    LojaID VARCHAR(255) NOT NULL PRIMARY KEY,
    VendedorID VARCHAR(255) NOT NULL,
    NomeLoja VARCHAR(255) NOT NULL,
    Descrição TEXT,
    EndereçoLoja VARCHAR(255),
    FOREIGN KEY (VendedorID) REFERENCES Clientes(ClienteID)
);