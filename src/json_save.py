import json

from src.files.base_file import BaseJsonSaver
from src.vacancies import Vacancies


class JSONSaver(BaseJsonSaver):
    """Класс для сохранения, добавления и изменения вакансий в json-файле"""

    def __init__(self, file_saver: str = "..data/filtered_vacancies.json"):
        """Констркутор, инициализирует путь до файла (для работы с ним)"""
        self.__file_saver = file_saver

    def load_json(self):
        """Метод получения данных из файла"""
        with open(self.__file_saver, encoding="utf-8") as file:
            json_file = json.load(file)
            return json_file

    @staticmethod
    def load_info_json(file_path):
        """Метод получения данных из файла"""
        with open(file_path, encoding="utf-8") as file:
            json_file = json.load(file)
            return json_file

    def add_vacancy(self, vacancies: Vacancies | dict):
        """Метод добавления вакансий в файл json"""
        with open(self.__file_saver, "r+", encoding="utf-8") as file:
            try:
                json.load(file)
            except json.JSONDecodeError:
                file.write("[]")

        with open(self.__file_saver, "r+", encoding="utf-8") as file:
            json_file_vacancies = json.load(file)

            dict_vacancy = {
                "name": vacancies.name,
                "url": vacancies.url,
                "salary": vacancies.salary,
                "snippet": vacancies.description,
            }

            if dict_vacancy not in json_file_vacancies:
                json_file_vacancies.append(dict_vacancy)

        with open(self.__file_saver, "w", encoding="utf-8") as file:
            json.dump(json_file_vacancies, file, ensure_ascii=False, indent=4)

    def delete_vacancy(self, vacancies: Vacancies):
        """Метод удаления вакансий из файла json"""
        with open(self.__file_saver, "r+", encoding="utf-8") as file:
            json_file_vacancies = json.load(file)

            dict_vacancy = {
                "name": vacancies.name,
                "url": vacancies.url,
                "salary": vacancies.salary,
                "snippet": vacancies.description,
            }

            if dict_vacancy in json_file_vacancies:
                json_file_vacancies.remove(dict_vacancy)

        with open(self.__file_saver, "w", encoding="utf-8") as file:
            json.dump(json_file_vacancies, file, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    vacancy = Vacancies("Программист", "<https://hh.ru/vacancy/123456>", "60000 - 140000",
                       "Требования: опыт работы от 1-3 лет...")

    json_saver = JSONSaver("../data/filtered_vacancies.json")
    json_saver.add_vacancy(vacancy)
    # json_saver.delete_vacancy(vacancy)