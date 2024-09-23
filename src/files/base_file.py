from abc import ABC, abstractmethod

from src.vacancies import Vacancies


class VacancyRepository(ABC):
    """Создаем абстрактный класс для чтения записи и удаления файла """
    @abstractmethod
    def add_vacancy(self, vacancy: Vacancies):
        """Добавить вакансию в файл."""
        pass

    @abstractmethod
    def get_vacancies(self, query: str):
        """Получить вакансии по заданным критериям."""
        pass

    @abstractmethod
    def delete_vacancy(self):
        """Удалить вакансию по идентификатору."""
        pass