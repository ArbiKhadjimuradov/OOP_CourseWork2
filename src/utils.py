import os
from typing import Any

from src.vacancies import Vacancies


def top_vacancies(vacancies_salary: Any, top_n: Any):
    """Функция выводящая топ вакансий"""
    vacancies_top = sorted(vacancies_salary, key=lambda x: x.salary, reverse=True)[:top_n]
    return vacancies_top


def filter_keyword(vacancies: Any, keywords: Any):
    if isinstance(keywords, list) and keywords:
        vacancies_keyword = [
            vacancy for vacancy in vacancies
            if all(word.lower() in vacancy.description.lower() for word in keywords)
        ]
        return vacancies_keyword
    return vacancies


def filter_salary(vacancies_keyword: Any, salary: Any):
    vacancies_salary = []
    for v in vacancies_keyword:
        if int(salary) <= v.salary:
            vacancies_salary.append(v)
    return vacancies_salary


def display_vacancies(vacancies_top: Any):
    """Отображает информацию о вакансиях для пользователя"""
    if not vacancies_top:
        print("Вакансии не найдены.")
        return

    for idx, vacancy in enumerate(vacancies_top, start=1):
        print(f"{idx}. {vacancy.name}")
        print(f"   URL: {vacancy.url}")
        salary = vacancy.salary
        if salary:
            print(f"   Нижний порог зарплаты : {salary}")
        else:
            print("   Зарплата не указана")
        print(f"   Описание: {vacancy.description}\n")


def save_filtered_vacancies(vacancies_top: Any, repository):
    """Сохраняет отфильтрованные вакансии в файл JSON."""
    if not vacancies_top:
        print("Нет вакансий для сохранения.")
        return
    os.makedirs(os.path.dirname(repository.file_path), exist_ok=True)
    # Сохраняем вакансии, преобразуя их в словари
    repository.save_data([vacancy.__dict__ for vacancy in vacancies_top])