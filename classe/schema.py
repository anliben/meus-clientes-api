from typing import Optional
from pydantic import BaseModel


class ProdutoBase(BaseModel):
    nome_produto: str
    valor: int
    quantidade: int
    estabelecimento: int


class ProdutoAdd(ProdutoBase):
    produto_id: str

    class Config:
        orm_mode = True


class Produto(ProdutoAdd):
    id: int

    class Config:
        orm_mode = True


class UpdateProduto(BaseModel):

    nome_produto: str
    valor: int
    quantidade: int
    estabelecimento: int

    class Config:
        orm_mode = True


'''------------------------------------------------------'''


class ClienteBase(BaseModel):

    nome_cliente: str
    whatsapp: str
    estabelecimento: int
    pedido: int


class ClienteAdd(ClienteBase):
    cliente_id: Optional[str] = None

    class Config:
        orm_mode = True


class Cliente(ClienteAdd):
    id: int

    class Config:
        orm_mode = True


class UpdateCliente(BaseModel):

    nome_cliente: str
    whatsapp: str
    estabelecimento: int
    pedido: int

    class Config:
        orm_mode = True


'''------------------------------------------------------------'''


class EstabelecimentoBase(BaseModel):

    nome_estabelecimento: str


class EstabelecimentoAdd(EstabelecimentoBase):
    estabelecimento_id: str

    class Config:
        orm_mode = True


class Estabelecimento(EstabelecimentoAdd):
    id: int

    class Config:
        orm_mode = True


class UpdateEstabelecimento(BaseModel):

    nome_estabelecimento: str

    class Config:
        orm_mode = True


'''------------------------------------------------------'''


class PedidoBase(BaseModel):

    nome_pedido: str
    cliente: str
    valor: str
    horario: str
    estabelecimento: str
    produtos: str
    # Falta complepar aqui'''

    '''[{  id: 12424,
          nome: str,
          valor: 100,
          quantidade:,
          estabelecimento: }]'''

    serveur: str
    tipo_pagamento: str
    pedido_pago: str
    pedido_em_aberto: str
    pedido_entregue: str


class PedidoAdd(PedidoBase):
    pedido_id: str

    class Config:
        orm_mode = True


class Pedido(PedidoAdd):
    id: int

    class Config:
        orm_mode = True


class UpdatePedido(BaseModel):
    nome_pedido: str
    cliente: str
    valor: str
    horario: str
    estabelecimento: str
    produtos: str

    # Falta complepar aqui'''

    '''[{  id: 12424,
          nome: str,
          valor: 100,
          quantidade:,
          estabelecimento: }]'''

    serveur: str
    tipo_pagamento: str
    pedido_pago: str
    pedido_em_aberto: str
    pedido_entregue: str

    class Config:
        orm_mode = True
