from database import SessionLocal, Analista, Equipamento

db = SessionLocal()

analistas_nomes = ["Ana", "Pedro", "João", "Mariana", "Roberto"]
analistas_objs = []

for nome in analistas_nomes:
    a = Analista(nome=nome)
    db.add(a)
    analistas_objs.append(a)

db.commit() 

equipamentos = [
    {"modelo": "Notebook Dell Latitude", "dono": analistas_objs[0]},
    {"modelo": "Monitor LG 29'", "dono": analistas_objs[0]},
    {"modelo": "MacBook Pro", "dono": analistas_objs[1]},
    {"modelo": "Teclado Mecânico", "dono": analistas_objs[1]},
    {"modelo": "Monitor Samsung 24'", "dono": analistas_objs[2]},
    {"modelo": "Headset Poly", "dono": analistas_objs[3]},
]

for eq in equipamentos:
    novo_eq = Equipamento(modelo=eq["modelo"], dono=eq["dono"])
    db.add(novo_eq)

db.commit()
db.close()
print("Banco de dados populado com sucesso!")