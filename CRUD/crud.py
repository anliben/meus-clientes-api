from sqlalchemy.orm import Session
import classe.model as model
import classe.schema as schema
from typing import Optional


def get_produto_by_produto_id(db: Session, produto_id: Optional[str] = None):

    return db.query(model.Produtos).filter(model.Produtos.produto_id ==
                                           produto_id).first()


def get_produto_by_id(db: Session, sl_id: int):

    return db.query(model.Produtos).filter(model.Produtos.id == sl_id).first()


def get_produtos(db: Session, skip: int = 0, limit: int = 100):

    return db.query(model.Produtos).offset(skip).limit(limit).all()


def add_produto_details_to_db(db: Session, produto: schema.ProdutoAdd):
    """ data_details = model.Produtos(
         produto_id=produto.produto_id,
         nome_produto=produto.nome_produto,
         foto_produto=produto.foto_produto,
         url=produto.url,
         plataform=produto.plataform,
         tecnolgy=produto.tecnolgy,
         squad=produto.squad,
         link=produto.link"""

    data_details = model.Produtos(
        produto_id=produto.produto_id,
        nome_produto=produto.nome_produto,
        valor=produto.valor,
        quantidade=produto.quantidade,
        estabelecimento=produto.estabelecimento

    )
    db.add(data_details)
    db.commit()
    db.refresh(data_details)
    return model.Produtos(**produto.dict())


def update_produto_details(db: Session, sl_id: int, details: schema):

    db.query(model.Produtos).filter(
        model.Produtos.id == sl_id).update(vars(details))
    db.commit()
    return db.query(model.Produtos).filter(model.Produtos.id == sl_id).first()


def delete_produto_details_by_id(db: Session, sl_id: int):

    try:
        db.query(model.Produtos).filter(model.Produtos.id == sl_id).delete()
        db.commit()
    except Exception as e:
        raise Exception(e)


'''--------------------------------------------------------------------'''


def get_cliente_by_cliente_id(db: Session, cliente_id: Optional[str] = None):

    return db.query(model.Clientes).filter(model.Clientes.cliente_id ==
                                           cliente_id).first()


def get_cliente_by_id(db: Session, sl_id: int):

    return db.query(model.Clientes).filter(model.Clientes.id == sl_id).first()


def get_clientes(db: Session, skip: int = 0, limit: int = 100):

    return db.query(model.Clientes).offset(skip).limit(limit).all()


def add_cliente_details_to_db(db: Session, cliente: schema.ClienteAdd):

    data_details = model.Clientes(
        cliente_id=cliente.cliente_id,
        nome_cliente=cliente.nome_cliente,
        whatsapp=cliente.whatsapp,
        estabelecimento=cliente.estabelecimento,
        pedido=cliente.pedido,
    )
    db.add(data_details)
    db.commit()
    db.refresh(data_details)
    return model.Clientes(**cliente.dict())


def update_cliente_details(db: Session, sl_id: int, details: schema):

    db.query(model.Clientes).filter(
        model.Clientes.id == sl_id).update(vars(details))
    db.commit()
    return db.query(model.Clientes).filter(model.Clientes.id == sl_id).first()


def delete_cliente_details_by_id(db: Session, sl_id: int):

    try:
        db.query(model.Clientes).filter(model.Clientes.id == sl_id).delete()
        db.commit()
    except Exception as e:
        raise Exception(e)


'''--------------------------------------------------------------------'''


def get_estabelecimento_by_estabelecimento_id(db: Session, estabelecimento_id:
                                              Optional[str] = None):

    return db.query(model.Estabelecimentos).filter(model.Estabelecimentos.
                                                   estabelecimento_id ==
                                                   estabelecimento_id).first()


def get_estabelecimento_by_id(db: Session, sl_id: int):

    return db.query(model.Estabelecimentos).filter(model.Estabelecimentos.id ==
                                                   sl_id).first()


def get_estabelecimentos(db: Session, skip: int = 0, limit: int = 100):

    return db.query(model.Estabelecimentos).offset(skip).limit(limit).all()


def add_estabelecimento_details_to_db(db: Session, estabelecimento: schema.
                                      EstabelecimentoAdd):

    data_details = model.Estabelecimentos(
        estabelecimento_id=estabelecimento.estabelecimento_id,
        nome_estabelecimento=estabelecimento.nome_estabelecimento

    )
    db.add(data_details)
    db.commit()
    db.refresh(data_details)
    return model.Estabelecimentos(**estabelecimento.dict())


def update_estabelecimento_details(db: Session, sl_id: int, details: schema):

    db.query(model.Estabelecimentos).filter(
        model.Estabelecimentos.id == sl_id).update(vars(details))
    db.commit()
    return db.query(model.Estabelecimentos).filter(model.Estabelecimentos.id ==
                                                   sl_id).first()


def delete_estabelecimento_details_by_id(db: Session, sl_id: int):

    try:
        db.query(model.Estabelecimentos).filter(
            model.Estabelecimentos.id == sl_id).delete()
        db.commit()
    except Exception as e:
        raise Exception(e)


'''--------------------------------------------------------------------'''


def get_pedido_by_pedido_id(db: Session, pedido_id: Optional[str] = None):

    return db.query(model.Pedidos).filter(model.Pedidos.pedido_id ==
                                          pedido_id).first()


def get_pedido_by_id(db: Session, sl_id: int):

    return db.query(model.Pedidos).filter(model.Pedidos.id == sl_id).first()


def get_pedidos(db: Session, skip: int = 0, limit: int = 100):

    return db.query(model.Pedidos).offset(skip).limit(limit).all()


def add_pedido_details_to_db(db: Session, pedido: schema.PedidoAdd):

    data_details = model.Pedidos(
        pedido_id=pedido.pedido_id,
        nome_pedido=pedido.nome_pedido,
        cliente=pedido.cliente,
        valor=pedido.valor,
        horario=pedido.horario,
        estabelecimento=pedido.estabelecimento,
        produtos=pedido.produtos,
        # Falta complepar aqui'''
        serveur=pedido.serveur,
        tipo_pagamento=pedido.tipo_pagamento,
        pedido_pago=pedido.pedido_pago,
        pedido_em_aberto=pedido.pedido_em_aberto,
        pedido_entregue=pedido.pedido_entregue,
    )
    db.add(data_details)
    db.commit()
    db.refresh(data_details)
    return model.Pedidos(**pedido.dict())


def update_pedido_details(db: Session, sl_id: int, details: schema):

    db.query(model.Pedidos).filter(
        model.Pedidos.id == sl_id).update(vars(details))
    db.commit()
    return db.query(model.Pedidos).filter(model.Pedidos.id == sl_id).first()


def delete_pedido_details_by_id(db: Session, sl_id: int):

    try:
        db.query(model.Pedidos).filter(model.Pedidos.id == sl_id).delete()
        db.commit()
    except Exception as e:
        raise Exception(e)
