from pydantic import BaseModel
from datetime import datetime



class TariffBase(BaseModel):
    name: str
    max_weight: float
    delivery_time_days: int


class Tariff(TariffBase):
    class Config:
        from_attributes = True


class DeliveryBase(BaseModel):
    id: int
    phone: str
    delivery_time: datetime
    car_number: str
    courier: str


class Delivery(DeliveryBase):
    class Config:
        from_attributes = True
