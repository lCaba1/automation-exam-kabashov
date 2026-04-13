from sqlalchemy.orm import Session
from db.models import Tariff, Delivery
from exceptions.exceptions import DeliveryNotFoundException 


def get_tariffs(db: Session):
    return db.query(Tariff).all()


def get_delivery(db: Session, phone: str, id: int):
    delivery = db.query(Delivery).filter(Delivery.phone == phone, Delivery.id == id).first()
    if not delivery:
        raise DeliveryNotFoundException("Аутентификация не пройдена")
    return delivery