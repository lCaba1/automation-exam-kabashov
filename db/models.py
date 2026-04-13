from sqlalchemy import Column, Integer, String, Float, DateTime
from db.database import Base


class Tariff(Base):
    __tablename__ = "tariffs"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    max_weight = Column(Float, nullable=False)
    delivery_time_days = Column(Integer, nullable=False)


class Delivery(Base):
    __tablename__ = "deliveries"

    id = Column(Integer, primary_key=True, index=True)
    address = Column(String, nullable=False)
    recipient = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    delivery_time = Column(DateTime, nullable=False)
    car_number = Column(String, nullable=False)
    courier = Column(String, nullable=False)
