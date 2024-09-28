from abc import ABC, abstractmethod


class AbstractAPI(ABC):
    @abstractmethod
    def connect(self):
        """Подключение к API."""
        pass

    @abstractmethod
    def get_vacancies(self, query: str, area=None, page=0):
        """Получение вакансий по запросу.

        :param query: Запрос для поиска вакансий.
        :param area: ID региона для поиска (опционально).
        :param page: Номер страницы результата (опционально).
        :return: Список вакансий.
        """
        pass