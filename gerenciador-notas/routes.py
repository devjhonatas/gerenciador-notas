#API rotas

from flask import request, jsonify
from models import Student, db

def configure_routes(app):
    @app.route('/students', methods=['GET'])
    def get_students():
        students = Student.query.all()
        return jsonify([{'id': s.id, 'name': s.name, 'grade': s.grade} for s in students])

    @app.route('/students', methods=['POST'])
    def add_student():
        data = request.get_json()
        new_student = Student(name=data['name'], grade=data['grade'])
        db.session.add(new_student)
        db.session.commit()
        return jsonify({'id': new_student.id}), 201
