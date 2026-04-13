from sqlalchemy.orm import Session
from db.database import SessionLocal
from db.models import Tariff, Delivery
from datetime import datetime


def seed_db():
    db: Session = SessionLocal()

    if db.query(Tariff).first():
        print("База уже заполнена")
        db.close()
        return

    tariffs = [
        Tariff(id=1, name="Черепаха", max_weight=10, delivery_time_days=30),
        Tariff(id=2, name="Волк", max_weight=5, delivery_time_days=10),
        Tariff(id=3, name="Орел", max_weight=2, delivery_time_days=5),
        Tariff(id=4, name="Гепард", max_weight=2, delivery_time_days=1),
    ]

    db.add_all(tariffs)
    db.commit()

    deliveries = [
        Delivery(
            id=1,
            address="Беговая, 3",
            recipient="Рунов",
            phone="+7561857361",
            delivery_time=datetime(2023, 1, 11, 16, 0),
            car_number="а712ее99",
            courier="Корунов Александр Владимирович",
        ),
        Delivery(
            id=2,
            address="Аргуновская, 6",
            recipient="Корунов",
            phone="+7917465162",
            delivery_time=datetime(2023, 1, 11, 15, 0),
            car_number="а171мр97",
            courier="Рунов Дмитрий Борисович",
        ),
        Delivery(
            id=3,
            address="Академика Анохина, 9",
            recipient="Сачков",
            phone="+7917562471",
            delivery_time=datetime(2023, 1, 11, 19, 0),
            car_number="м196ос50",
            courier="Косачков Кирилл Павлович",
        ),
    ]

    db.add_all(deliveries)
    db.commit()

    db.close()
    print("База успешно инициализирована")