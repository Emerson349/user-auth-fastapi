from fastapi import APIRouter, Depends, HTTPException
from ..models.order import Order
from ..models.user import User
from ..schemas import Order_create, Order_read
from sqlalchemy.orm import Session
from ..db.dependencies import get_db, verify_token

order_route = APIRouter(prefix="/orders", tags=["order"], dependencies=[verify_token])

@order_route.post("/order")
async def create_order(order: Order_create, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == order.user).first()
    if not user:
        raise HTTPException(404, "Usuario não cadastrado")

    new_order = Order(user=order.user)
    db.add(new_order)
    db.commit()
    return {"mensagem": f"pedido de {user.name} cadastrado! Id do pedido: {new_order.id}"}

@order_route.post("/order/cancel/{order_id}")
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