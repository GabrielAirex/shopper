CREATE TYPE public.tipo_cliente AS ENUM ('comprador', 'vendedor');

CREATE TABLE public.Clientes (
    ClienteID VARCHAR(255) NOT NULL PRIMARY KEY,
    Nome VARCHAR(255) NOT NULL,
    Email VARCHAR(255) NOT NULL,
    Telefone VARCHAR(20),
    Endereço VARCHAR(255),
    TipoCliente tipo_cliente NOT NULL
);