from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

engine = create_engine("sqlite:///inventario.db", echo=True)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class Analista(Base):
    __tablename__ = "analistas"
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    
    equipamentos = relationship("Equipamento", back_populates="dono")

class Equipamento(Base):
    __tablename__ = "equipamentos"
    id = Column(Integer, primary_key=True)
    modelo = Column(String)
    analista_id = Column(Integer, ForeignKey("analistas.id"))
    
    dono = relationship("Analista", back_populates="equipamentos")

Base.metadata.create_all(engine)