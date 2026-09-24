from app import app
from models import db, Usuario, Curso

with app.app_context():
    db.create_all()

    if Usuario.query.count() == 0:
        db.session.add_all([
            Usuario(username="juan", password="1234"),
            Usuario(username="maria", password="abcd"),
            Usuario(username="pedro", password="2026"),
        ])

    if Curso.query.count() == 0:
        db.session.add_all([
            Curso(nombre="Programación Web", docente="Luis Pérez", cupos=15),
            Curso(nombre="Bases de Datos", docente="Ana López", cupos=8),
            Curso(nombre="Inteligencia Artificial", docente="Carlos Rojas", cupos=0),
        ])

    db.session.commit()
    print("✅ Base de datos inicializada")