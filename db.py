from sqlalchemy import create_engine  #создадим сущьность которая будет запускать нашу БД
from sqlalchemy.orm import sessionmaker, DeclarativeBase # загружаем дополнительно сущьности для работы
from sqlalchemy import Column, Integer, String


engine = create_engine("sqlite:///taskmanager.db", echo=True)

SessionLocal = sessionmaker(bind=engine)

class Basa(DeclarativeBase):
    pass