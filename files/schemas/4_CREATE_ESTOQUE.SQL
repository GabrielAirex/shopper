CREATE TABLE public.Estoque (
    ProdutoID VARCHAR(255) NOT NULL,
    LojaID VARCHAR(255) NOT NULL,
    Quantidade INT NOT NULL,
    FOREIGN KEY (ProdutoID, LojaID) REFERENCES ProdutosLojas(ProdutoID, LojaID),
    PRIMARY KEY (ProdutoID, LojaID)
);