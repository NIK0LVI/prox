import pytest
from datetime import date
from sqlalchemy.exc import IntegrityError

from app.tests import TestClass, TestingSessionLocal
from app.students.repository import StudentRepository


class TestStudentRepo(TestClass):

    def create_students_for_methods(self):
        with TestingSessionLocal() as db:
            student_repo = StudentRepository(db)
            student_1 = student_repo.create_student("prezime_1", "ime_1", "telefon_1", "adresa_1", "grad_1",
                                                    "postanski_1",
                                                    "rezultat_1",
                                                    date, date)
            student_2 = student_repo.create_student("prezime_2", "ime_2", "telefon_2", "adresa_2", "grad_2",
                                                    "postanski_2",
                                                    "rezultat_2",
                                                    date, date)

    def test_create_student(self):
        with TestingSessionLocal() as db:
            student_repo = StudentRepository(db)
            student = student_repo.create_student("prezime", "ime", "telefon", "adresa", "grad", "postanski",
                                                  "rezultat",
                                                  date, date)
            assert student.last_name == "prezime"
            assert student.first_name == "ime"
            assert student.phone == "telefon"
            assert student.city == "grad"
            assert student.postal == "postanski"
            assert student.course_score == "rezultat"
            assert student.course_start == date
            assert student.course_end == date

    def test_create_student_error(self):
        with TestingSessionLocal() as db:
            student_repo = StudentRepository(db)
            student = student_repo.create_student("prezime", "ime", "telefon", "adresa", "grad", "postanski",
                                                  "rezultat",
                                                  date, date)
            assert not student.last_name != "prezime"
            assert not student.first_name != "ime"
            assert not student.phone != "telefon"
            assert not student.city != "grad"
            assert not student.postal != "postanski"
            assert not student.course_score != "rezultat"
            assert not student.course_start != date
            assert not student.course_end != date
            with pytest.raises(IntegrityError) as e:
                student_1 = student_repo.create_student("prezime_1", "ime_1", "telefon_1", "adresa_1", "grad_1",
                                                        "postanski_1",
                                                        "rezultat_1",
                                                        date, date)

    def test_get_all_students(self):
        self.create_students_for_methods()
        with TestingSessionLocal() as db:
            students = StudentRepository(db)
            all_students = students.get_all_students()
            assert len(all_students) == 4
