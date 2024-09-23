from src.hh_ru_api import HH_API
from src.open import PATH_TO_FILE
from src.utils import (display_vacancies, filter_keyword, filter_salary,
                       save_filtered_vacancies, top_vacancies)
from src.files.file_hh_data import JsonVacancyRepository


def user_interaction() -> None:
    hh_api = HH_API()
    hh_api.connect()

    print("Добро пожаловать в систему поиска вакансий!")
    while True:
        query = input("Введите поисковый запрос (или 'exit' для выхода): ")
        if query.lower() == 'exit':
            break

        top_n = input("Введите количество вакансий для вывода в топ N (0 для пропуска): ")
        top_n = int(top_n) if top_n.isdigit() else None

        keyword = input("Введите ключевое слово для поиска в описании (или пропустите, нажав Enter): ").split()

        salary = input("Введите нижний порог зарплаты: ")

        vacancies = hh_api.get_vacancies(query)
        print(vacancies)

        vacancies_keyword = filter_keyword(vacancies, keyword)

        vacancies_salary = filter_salary(vacancies_keyword, salary)

        vacancies_top = top_vacancies(vacancies_salary, top_n)

        result = display_vacancies(vacancies_top)

        file_path = PATH_TO_FILE
        repository = JsonVacancyRepository(file_path)
        save_filtered_vacancies(vacancies_top, repository)

        return result


if __name__ == '__main__':
    user_interaction()