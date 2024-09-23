import json
from typing import Any

from src.hh_ru_api import HH_API
from src.open import PATH_TO_FILE
from src.vacancies import Vacancies
from src.files.base_file import VacancyRepository


class JsonVacancyRepository(VacancyRepository):
    """Класс работы с файлами"""
    file = PATH_TO_FILE

    def __init__(self, __file_path=file):
        self.file_path = __file_path

    def _load_data(self):
        """Считывает данные из файла."""
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                vacancies = json.load(f)
                return vacancies
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_data(self, vacancies: Any):
        """Сохраняет данные в файл."""
        with open(self.file_path, 'w+', encoding='utf-8') as f:

            json.dump(vacancies, f, ensure_ascii=False, indent=4)

    def add_vacancy(self, vacancy: Vacancies):
        """Добавляем вакансию в файл."""
        vacancies = self._load_data()
        vacancies.append(vacancy)
        self.save_data(vacancies)

    def get_vacancies(self, criteria):
        """Получаем вакансии по заданным критериям."""
        vacancies = self._load_data()
        return [vacancy for vacancy in vacancies if all(item in vacancy.items() for item in criteria.items())]

    def delete_vacancy(self):
        """Удаляем вакансию """
        with open(self.file_path, 'w+', encoding='utf-8') as f:
            pass


# Пример использования
if __name__ == "__main__":
    hh_api = HH_API()
    hh_api.connect()
    repository = JsonVacancyRepository()