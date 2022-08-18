from sqlalchemy import Column, Integer, String
from DATABASE.db_handler import Base


class Produtos(Base):

    __tablename__ = "produto"
    id = Column(Integer, primary_key=True, autoincrement=True,
                index=True, nullable=False)
    produto_id = Column(String, unique=True, index=True, nullable=False)
    nome_produto = Column(String(255), index=True, nullable=False)
    estabelecimento = Column(Integer)
    quantidade = Column(Integer)
    valor = Column(Integer)


'''--------------------------------------------------------------'''


class Estabelecimentos(Base):

    __tablename__ = "estabelecimento"
    id = Column(Integer, primary_key=True, autoincrement=True,
                index=True, nullable=False)
    estabelecimento_id = Column(
        String, unique=True, index=True, nullable=False)
    nome_estabelecimento = Column(String(255), index=True, nullable=False)


'''-------------------------------------------------------------------'''


class Clientes(Base):

    __tablename__ = "cliente"
    id = Column(Integer, primary_key=True, autoincrement=True,
                index=True, nullable=False)
    cliente_id = Column(String(255), unique=True, index=True, nullable=False)
    nome_cliente = Column(String(255), index=True, nullable=False)
    whatsapp = Column(Integer)
    estabelecimento = Column(Integer)
    pedido = Column(Integer)


'''-------------------------------------------------------------------'''


class Pedidos(Base):

    __tablename__ = "pedido"
    id = Column(Integer, primary_key=True, autoincrement=True,
                index=True, nullable=False)
    pedido_id = Column(String(255), unique=True, index=True, nullable=False)
    nome_pedido = Column(String(255), index=True, nullable=False)
    cliente = Column(String)
    valor = Column(String)
    horario = Column(String)
    estabelecimento = Column(Integer)
    produtos = Column(String)
    '''Falta complepar aqui'''

    serveur = Column(String)
    tipo_pagamento = Column(String)
    pedido_pago = Column(String)
    pedido_em_aberto = Column(String)
    pedido_entregue = Column(String)
