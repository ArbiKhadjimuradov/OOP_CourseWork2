from src.vacancies import Vacancies


def test_initialization_with_salary(vacancy_with_salary):
    assert vacancy_with_salary.name == "Программист"
    assert vacancy_with_salary.salary == 100000
    assert vacancy_with_salary.description == "Разработка ПО"
    assert vacancy_with_salary.url == "http://example.com"


def test_initialization_without_salary(vacancy_without_salary):
    assert vacancy_without_salary.name == "Программист"
    assert vacancy_without_salary.salary == "Зарплата не указана"
    assert vacancy_without_salary.description == "Разработка ПО"
    assert vacancy_without_salary.url == "http://example.com"


def test_initialization_with_empty_description():
    vacancy = Vacancies("Программист", 100000, "", "http://example.com")
    assert vacancy.name == "Программист"
    assert vacancy.salary == 100000
    assert vacancy.description == ""
    assert vacancy.url == "http://example.com"


def test_initialization_with_empty_url():
    vacancy = Vacancies("Программист", 100000, "Разработка ПО", "")
    assert vacancy.name == "Программист"
    assert vacancy.salary == 100000
    assert vacancy.description == "Разработка ПО"
    assert vacancy.url == ""