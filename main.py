from pprint import pprint
from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import CRUD.crud as crud
import classe.model as model
import classe.schema as schema
from DATABASE.db_handler import SessionLocal, engine

model.Base.metadata.create_all(bind=engine)

# initcializa o app
app = FastAPI(
    title="Anliben Services Pro",
    description="Você pode executar a operação CRUD usando esta API",
    version="1.0.0"
)


# Dependência
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/clientes/all',
         response_model=List[schema.Cliente], tags=['clientes'])
def retrieve_all_clientes_details(skip: int = 0, limit: int = 100,
                                  db: Session = Depends(get_db)):
    clientes = crud.get_clientes(db=db, skip=skip, limit=limit)
    return clientes


@app.post('/clientes/add', response_model=schema.ClienteAdd, tags=['clientes'])
def add_new_cliente(cliente: schema.ClienteAdd, db: Session = Depends(get_db)):
    pprint(cliente)
    dir(cliente)
    cliente_id = crud.get_cliente_by_cliente_id(
        db=db,
        cliente_id=cliente.cliente_id)
    if cliente_id:
        raise HTTPException(
            status_code=400,
            detail=f"Cliente id {cliente.cliente_id} already exist in database: {cliente_id}"
        )
    return crud.add_cliente_details_to_db(db=db, cliente=cliente)


@app.delete('/clientes/delete', tags=['clientes'])
def delete_cliente_by_id(sl_id: int, db: Session = Depends(get_db)):
    details = crud.get_cliente_by_id(db=db, sl_id=sl_id)
    if not details:
        raise HTTPException(
            status_code=404, detail=f"No record found to delete")

    try:
        crud.delete_cliente_details_by_id(db=db, sl_id=sl_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Unable to delete: {e}")
    return {"delete status": "success"}


@app.put('/clientes/update', response_model=schema.Cliente, tags=['clientes'])
def update_cliente_details(sl_id: int, update_param: schema.UpdateCliente,
                           db: Session = Depends(get_db)):
    details = crud.get_cliente_by_id(db=db, sl_id=sl_id)
    if not details:
        raise HTTPException(status_code=404,
                            detail=f"No record found to update")

    return crud.update_cliente_details(db=db, details=update_param,
                                       sl_id=sl_id)


# produtos

@app.get('/produtos/all', response_model=List[schema.Produto], tags=['produtos'])
def retrieve_all_produtos_details(skip: int = 0, limit: int = 100,
                                  db: Session = Depends(get_db)):
    produtos = crud.get_produtos(db=db, skip=skip, limit=limit)
    return produtos


@app.post('/produto/add', response_model=schema.ProdutoAdd, tags=['produtos'])
def add_new_produto(produto: schema.ProdutoAdd, db: Session = Depends(get_db)):
    pprint(produto)
    dir(produto)
    produto_id = crud.get_produto_by_produto_id(
        db=db,
        produto_id=produto.produto_id)
    if produto_id:
        raise HTTPException(
            status_code=400,
            detail=f"Produto id {produto.produto_id} already exist in database:{produto_id}"
        )
    return crud.add_produto_details_to_db(db=db, produto=produto)


@app.delete('/produto/delete', tags=['produtos'])
def delete_produto_by_id(sl_id: int, db: Session = Depends(get_db)):
    details = crud.get_produto_by_id(db=db, sl_id=sl_id)
    if not details:
        raise HTTPException(
            status_code=404, detail=f"No record found to delete")

    try:
        crud.delete_produto_details_by_id(db=db, sl_id=sl_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Unable to delete: {e}")
    return {"delete status": "success"}


@app.put('/produto/update', response_model=schema.Produto, tags=['produtos'])
def update_produto_details(sl_id: int, update_param: schema.UpdateProduto,
                           db: Session = Depends(get_db)):
    details = crud.get_produto_by_id(db=db, sl_id=sl_id)
    if not details:
        raise HTTPException(status_code=404,
                            detail=f"No record found to update")

    return crud.update_produto_details(db=db, details=update_param,
                                       sl_id=sl_id)


# Estabelecimento


@app.get('/estabelecimentos/all', response_model=List[schema.Estabelecimento],
         tags=['estabelecimentos'])
def retrieve_all_estabelecimentos_details(skip: int = 0, limit: int = 100,
                                          db: Session = Depends(get_db)):
    estabelecimentos = crud.get_estabelecimentos(db=db, skip=skip, limit=limit)
    return estabelecimentos


@app.post('/estabelecimento/add', response_model=schema.EstabelecimentoAdd,
          tags=['estabelecimentos'])
def add_new_estabelecimento(estabelecimento: schema.EstabelecimentoAdd, db: Session = Depends(get_db)):
    pprint(estabelecimento)
    dir(estabelecimento)
    estabelecimento_id = crud.get_estabelecimento_by_estabelecimento_id(
        db=db,
        estabelecimento_id=estabelecimento.estabelecimento_id)
    if estabelecimento_id:
        raise HTTPException(
            status_code=400,
            detail=f"Estabelecimento id {estabelecimento.estabelecimento_id} already exist in database: {estabelecimento_id}"
        )
    return crud.add_estabelecimento_details_to_db(db=db, estabelecimento=estabelecimento)


@app.delete('/estabelecimento/delete', tags=['estabelecimentos'])
def delete_estabelecimento_by_id(sl_id: int, db: Session = Depends(get_db)):
    details = crud.get_estabelecimento_by_id(db=db, sl_id=sl_id)
    if not details:
        raise HTTPException(
            status_code=404, detail=f"No record found to delete")

    try:
        crud.delete_estabelecimento_details_by_id(db=db, sl_id=sl_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Unable to delete: {e}")
    return {"delete status": "success"}


@app.put('/estabelecimento/update', response_model=schema.Estabelecimento,
         tags=['estabelecimentos'])
def update_estabelecimento_details(sl_id: int, update_param: schema.
                                   UpdateEstabelecimento,
                                   db: Session = Depends(get_db)):
    details = crud.get_estabelecimento_by_id(db=db, sl_id=sl_id)
    if not details:
        raise HTTPException(status_code=404,
                            detail=f"No record found to update")

    return crud.update_estabelecimento_details(db=db, details=update_param,
                                               sl_id=sl_id)

# Pedidos


@app.get('/pedidos/all', response_model=List[schema.Pedido], tags=['pedidos'])
def retrieve_all_pedidos_details(skip: int = 0, limit: int = 100,
                                 db: Session = Depends(get_db)):
    pedidos = crud.get_pedidos(db=db, skip=skip, limit=limit)
    return pedidos


@app.post('/pedidos/add', response_model=schema.PedidoAdd, tags=['pedidos'])
def add_new_pedido(pedido: schema.PedidoAdd, db: Session = Depends(get_db)):
    pprint(pedido)
    dir(pedido)
    pedido_id = crud.get_pedido_by_pedido_id(
        db=db,
        pedido_id=pedido.pedido_id)
    if pedido_id:
        raise HTTPException(
            status_code=400,
            detail=f"Pedido id {pedido.pedido_id} already exist in database: {pedido_id}"
        )
    return crud.add_pedido_details_to_db(db=db, pedido=pedido)


@app.delete('/pedido/delete', tags=['pedidos'])
def delete_pedido_by_id(sl_id: int, db: Session = Depends(get_db)):
    details = crud.get_pedido_by_id(db=db, sl_id=sl_id)
    if not details:
        raise HTTPException(
            status_code=404, detail=f"No record found to delete")

    try:
        crud.delete_pedido_details_by_id(db=db, sl_id=sl_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Unable to delete: {e}")
    return {"delete status": "success"}


@app.put('/pedido/update', response_model=schema.Pedido, tags=['pedidos'])
def update_pedido_details(sl_id: int, update_param: schema.UpdatePedido,
                          db: Session = Depends(get_db)):
    details = crud.get_pedido_by_id(db=db, sl_id=sl_id)
    if not details:
        raise HTTPException(status_code=404,
                            detail=f"No record found to update")

    return crud.update_pedido_details(db=db, details=update_param,
                                      sl_id=sl_id)
