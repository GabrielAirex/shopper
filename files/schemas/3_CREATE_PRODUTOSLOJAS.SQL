CREATE TABLE public.ProdutosLojas (
    ProdutoID VARCHAR(255) NOT NULL,
    LojaID VARCHAR(255) NOT NULL,
    PreçoEspecial DECIMAL(10, 2),
    CondiçõesEspeciais TEXT,
    Promocao BOOLEAN,
    FOREIGN KEY (ProdutoID) REFERENCES Produtos(ProdutoID),
    FOREIGN KEY (LojaID) REFERENCES Lojas(LojaID),
    PRIMARY KEY (ProdutoID, LojaID)
);
