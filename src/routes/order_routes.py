from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.models.order import Order
from src.models.user import User
from src.models.items import Item
from src.app.schemas import Order_create, Order_read, Item_schema
from src.db.dependencies import get_db, verify_token


order_route = APIRouter(prefix="/orders", tags=["order"], dependencies=[Depends(verify_token)])

@order_route.post("/order")
async def create_order(order: Order_create, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == order.user).first()
    if not user:
        raise HTTPException(404, "Usuario não cadastrado")

    new_order = Order(user=order.user)
    db.add(new_order)
    db.commit()
    return {"mensagem": f"pedido de {user.name} cadastrado! Id do pedido: {new_order.id}"}

@order_route.post("/order/cancel/{order_id}", response_model=Order_read)
async def cancel_order(order_id: int, db: Session = Depends(get_db), user: User = Depends(verify_token)):
    order = db.query(Order).filter(Order.id==order_id).first()
    if user.id != order.user and not user.admin:
        raise HTTPException(401, "Acesso negado")
    if not order:
        raise HTTPException(404, "pedido não cadastrado")
    order.status = "CANCELADO"
    db.commit()
    return{
        "mensagem": f"pedido {order_id} cancelado com sucesso!"
    }

@order_route.get("/order/list_orders", response_model=Item_schema)
async def get_orders(db: Session = Depends(get_db), user: User = Depends(verify_token)):
    if user.admin:
        orders = db.query(Order).all()
    else:
        orders = db.query(Order).filter(Order.user==user.id).all()
    return {
        "user": user.name,
        "orders": orders
    }

@order_route.post("/order/add-item/{order_id}")
async def add_item_order(order_id: int, item_schema: Item_schema, db: Session = Depends(get_db), user: User = Depends(verify_token)):
    order = db.query(Order).filter(Order.id==order_id).first()
    if not order:
        raise Exception(404, "Pedido não cadastrado")
    if user.id != order.user and not user.admin:
        raise Exception(401, "Acesso negado")
    item = Item(item_schema.name, item_schema.amount, item_schema.unit_price, item_schema.flavor, item_schema.size, order_id)
    order.update_price(item.unit_price * item.amount)
    db.add(item)
    db.commit()
    return {
        "mensagem": f"Item adicionado ao pedido de {user.name}",
        "item": item_schema
    }

@order_route.post("/order/finish-order")
async def finish_order(order_id: int, db: Session = Depends(get_db), user: User = Depends(verify_token)):
    order = db.query(Order).filter(Order.id==order_id).first()
    if not order:
        raise Exception(404, "Pedido não cadastrado")
    if user.id != order.user and not user.admin:
        raise Exception(401, "Acesso negado")
    order.status = "FINALIZADO" 
    return {
        "mensagem" : f"pedido {order_id} finalizado!",
        "preco total" : f"R$ {order.price}" 
    }