from abc import ABC, abstractmethod

from src.vacancies import Vacancies


class BaseJsonSaver(ABC):
    """Базовый класс, определяет методы добавления и удаления вакансий из файла"""

    @abstractmethod
    def add_vacancy(self: object, vacancies: Vacancies) -> None:
        """Абстрактный метод добавления вакансий в файл"""
        pass

    @abstractmethod
    def delete_vacancy(self: object, vacancies: Vacancies) -> None:
        """Абстрактный метод удаления вакансий из файла"""
        pass