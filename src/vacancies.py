class Vacancies:
    """Класс для работы с вакансиями"""
    __list_vacancies: list = []

    def __init__(self, name: str, salary: int, description: str, url: str):
        self.name = name
        self.salary = salary if salary is not None else "Зарплата не указана"
        self.description = description
        self.url = url

        __slots__ = ("name", "salary", "description, url")

    def __str__(self):
        return (f"Вакансия: {self.name}\n ссылка: {self.url}\n зарплата: {self.salary}\n "
                f"описание: {self.description}")

    def __validate(self, salary):
        """Метод валидации зарплаты"""
        if salary is not None:
            self.__salary = salary
            if type(salary) is str:
                salary_split = salary.split(" ")
                self.__salary = {"from": int(salary_split[0]), "to": int(salary_split[2])}
        else:
            self.__salary = {"from": 0, "to": 0}

        return self.__salary

    def __eq__(self, other: object) -> bool:
        """Сравнение вакансий по зарплате равно"""
        if not isinstance(other, Vacancies):
            return NotImplemented
        return self.salary == other.salary

    def __lt__(self, other: object) -> bool:
        """Сравнение вакансий по зарплате меньше"""
        if not isinstance(other, Vacancies):
            return NotImplemented
        if isinstance(self.salary, (int, float)) and isinstance(other.salary, (int, float)):
            return self.salary < other.salary
        return False

    def __repr__(self):
        return f"Vacancy(name='{self.name}', url='{self.url}', salary={self.salary}, description='{self.description}')"

    @classmethod
    def filtered_salary(cls, from_salary: int = 0, to_salary: int = float("inf")):
        """Метод фильтрации вакансий по зарплате (от и до вилка)"""
        for vacancies in cls.__list_vacancies:
            if vacancies["salary"].get("from", 0) >= from_salary and vacancies["salary"]["to"] <= to_salary:
                print(vacancies)


if __name__ == "__main__":
    vacancy1 = Vacancies("водитель", 80000, "водитель-дальнобойщик", "ссылка")
    vacancy2 = Vacancies("механик", 90000, "механик-универсал", "ссылка1")
    print(vacancy1)
    print(vacancy2 > vacancy1)