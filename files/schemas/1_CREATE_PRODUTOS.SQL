CREATE TABLE public.Produtos (
    ProdutoID VARCHAR(255) NOT NULL PRIMARY KEY,
    NomeProduto VARCHAR(255) NOT NULL,
    DescriçãoProduto TEXT,
    Preço DECIMAL(10, 2) NOT NULL
);