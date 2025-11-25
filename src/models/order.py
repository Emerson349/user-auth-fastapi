from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey
from sqlalchemy.orm import relationship
from ..db.init_db import Base
from sqlalchemy_utils import ChoiceType

class Order(Base):
    __tablename__ = "order"

    ORDER_STATUS = (
        ("PENDENTE", "PENDENTE"),
        ("CANCELADO", "CANCELADO"),
        ("FINALIZADO", "FINALIZADO")
    )

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    status = Column("status", ChoiceType(choices=ORDER_STATUS))
    user = Column("user", ForeignKey("user.id"), nullable=False)
    price = Column("price", Float)
    itens = relationship("Item", cascade="all, delete")

    def __init__(self, user, status="PENDENTE", price=0):
        self.status = status
        self.user = user
        self.price = price

    def update_price(self, valor: int):
        self.preco += valor