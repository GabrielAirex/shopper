CREATE TABLE public.AtributosProduto (
    AtributoID SERIAL PRIMARY KEY,
    ProdutoID VARCHAR(255) NOT NULL,
    NomeAtributo VARCHAR(255) NOT NULL,
    ValorAtributo TEXT,
    FOREIGN KEY (ProdutoID) REFERENCES Produtos(ProdutoID)
);