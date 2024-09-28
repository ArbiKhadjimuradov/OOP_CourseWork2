import pytest
from src.vacancies import Vacancies


@pytest.fixture
def vacancy_with_salary():
    """Фикстура для создания вакансии с указанной зарплатой"""
    return Vacancies("Программист", 100000, "Разработка ПО", "http://example.com")


@pytest.fixture
def vacancy_without_salary():
    """Фикстура для создания вакансии без указанной зарплаты"""
    return Vacancies("Программист", None, "Разработка ПО", "http://example.com")