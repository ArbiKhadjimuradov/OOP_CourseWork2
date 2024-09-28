import requests

from src.api import AbstractAPI
from src.vacancies import Vacancies


class HH_API(AbstractAPI):
    BASE_URL = "https://api.hh.ru/vacancies"

    def __init__(self):
        self.__session = requests.Session()
        self.__vacancies = []
        self.__vacancies_new = []

    def __connect(self):
        """Проверка подключения к API.
        делаем простой запрос к API
        следали метод приватным
        """
        response = self.__session.get(self.BASE_URL)
        if response.status_code == 200:
            print("Успешно подключено к hh.ru API")
        else:
            print("Не удалось подключиться к hh.ru API")
            response.raise_for_status()

    def connect(self):
        """Метод публичный обращается к приватному методу"""
        self.__connect()

    def get_vacancies(self, query: str, area=None, page=20):
        """Получение списка вакансий по заданному запросу."""
        params = {
            'text': query,
            'area': area,
            'page': page
        }
        response = self.__session.get(self.BASE_URL, params=params)
        if response.status_code == 200:
            vacancies = response.json().get('items', [])
            self.__vacancies.extend(vacancies)

            for v in self.__vacancies:
                if v["name"]:
                    name = v["name"]
                else:
                    name = "Название не указано"
                if v["alternate_url"]:
                    url = v["alternate_url"]
                else:
                    url = "Ссылка отсутствует"
                if v["salary"] is None or v["salary"]["from"] is None:
                    salary = 0
                else:
                    salary = v["salary"]["from"]
                if v["snippet"] is None or v["snippet"]["responsibility"] is None:
                    description = "Описание отсутствует"
                else:
                    description = v["snippet"]["responsibility"]

                self.__vacancies_new.append(
                    Vacancies(name=name, url=url, description=description, salary=salary)
                )
            return self.__vacancies_new

        else:
            print("Ошибка при получении вакансий:", response.status_code)
            response.raise_for_status()


if __name__ == "__main__":
    hh_api = HH_API()
    hh_api.connect()  # Проверка подключения

    # Запрос вакансий
    vacancies_new = hh_api.get_vacancies("Backend-разработчик")  # Поиск по всей России
    for v in vacancies_new:
        print(v)