CREATE TABLE public.RegistroVendas (
    VendaID VARCHAR(255) NOT NULL PRIMARY KEY,
    ProdutoID VARCHAR(255) NOT NULL,
    ClienteID VARCHAR(255) NOT NULL,
    LojaID VARCHAR(255) NOT NULL,
    Quantidade INT NOT NULL,
    DataVenda DATE NOT NULL,
    FOREIGN KEY (ProdutoID) REFERENCES Produtos(ProdutoID),
    FOREIGN KEY (ClienteID) REFERENCES Clientes(ClienteID),
    FOREIGN KEY (LojaID) REFERENCES Lojas(LojaID)
);