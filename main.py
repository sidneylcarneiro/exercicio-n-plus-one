from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, Analista, Equipamento

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/inventario/lento")
def listar_inventario_lento(db: Session = Depends(get_db)):
    analistas = db.query(Analista).all()
    
    resultado = []
    for analista in analistas:
        itens = [eq.modelo for eq in analista.equipamentos]
        resultado.append({"analista": analista.nome, "ativos": itens})
        
    return resultado

