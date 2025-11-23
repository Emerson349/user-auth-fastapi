from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey
from ..db.init_db import Base
from sqlalchemy_utils import ChoiceType

class Item(Base):
    __tablename__ = "item"

    SIZES = (
        ("SMALL", "SMALL"),
        ("MEDIUM", "MEDIUM"),
        ("BIG", "BIG")
    )

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String)
    amount = Column("amount", Integer)
    unit_price = Column("unit_price", Float, nullable=False)
    flavor = Column("flavor", String)
    size = Column("size", ChoiceType(choices=SIZES))
    order = Column("order", ForeignKey("order.id"))

    def __init__(self, name, amount, unit_price, flavor, size, order):
        self.name = name
        self.amount = amount
        self.unit_price = unit_price
        self.flavor = flavor
        self.size = size
        self.order = order




