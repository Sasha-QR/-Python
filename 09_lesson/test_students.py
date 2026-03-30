from models import SessionLocal, Student


def test_create_student():
    session = SessionLocal()
    try:
        student = Student(name="Test Student")

        session.add(student)
        session.commit()

        result = session.query(Student).filter_by(name="Test Student").first()
        assert result is not None

        # очистка
        session.delete(result)
        session.commit()
    finally:
        session.close()


def test_update_student():
    session = SessionLocal()
    try:
        student = Student(name="Old Name")
        session.add(student)
        session.commit()

        # обновление
        student.name = "New Name"
        session.commit()

        updated = session.query(Student).filter_by(id=student.id).first()
        assert updated.name == "New Name"

        # очистка
        session.delete(updated)
        session.commit()
    finally:
        session.close()


def test_delete_student():
    session = SessionLocal()
    try:
        student = Student(name="To Delete")
        session.add(student)
        session.commit()

        student_id = student.id

        # удаление
        session.delete(student)
        session.commit()

        result = session.query(Student).filter_by(id=student_id).first()
        assert result is None
    finally:
        session.close()