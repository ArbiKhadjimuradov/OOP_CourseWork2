from src.hh_ru_api import HH_API
from src.open import PATH_TO_FILE
from src.utils import (display_vacancies, filter_keyword, filter_salary, top_vacancies)
from src.json_save import JSONSaver
from src.vacancies import Vacancies


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
        JSONSaver(file_path)

        return result

    vacancy = Vacancies(
        "Python Developer",
        "<https://hh.ru/vacancy/123456>",
        "100 000-150 000 руб.",
        "Требования: опыт работы от 3 лет...",
    )

    Vacancies.validate_salary()
    # Сохранение информации о вакансиях в файл
    json_saver = JSONSaver()
    json_saver.add_vacancy(vacancy)
    json_saver.delete_vacancy(vacancy)

    #  циклом создаем каждый словарь обьектом класса Vacancy
    for filtered_vacancy in [tuple(d.values()) for d in top_vacancies]:
        vacancy_obj = Vacancies(*filtered_vacancy)
        json_saver.add_vacancy(vacancy_obj)


if __name__ == "__main__":
    user_interaction()