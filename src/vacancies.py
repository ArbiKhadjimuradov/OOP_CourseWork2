class Vacancies:
    """Класс для работы с вакансиями"""
    def __init__(self, name: str, salary: int, description: str, url: str):
        self.name = name
        self.salary = salary if salary is not None else "Зарплата не указана"
        self.description = description
        self.url = url

        __slots__ = ("name", "salary", "description, url")

    def __str__(self):
        return (f"Вакансия: {self.name}\n ссылка: {self.url}\n зарплата: {self.salary}\n "
                f"описание: {self.description}")

    def __validate(self):
        # Проверяем, указан ли заголовок вакансии
        if not isinstance(self.name, str) or not self.name.strip():
            raise ValueError("Название вакансии должно быть непустой строкой.")

        # Проверяем, указана ли ссылка на вакансию
        if not isinstance(self.url, str) or not self.url.strip():
            raise ValueError("Ссылка на вакансию должна быть непустой строкой.")

        # Проверяем зарплату
        if isinstance(self.salary, (int, float)) and self.salary < 0:
            raise ValueError("Зарплата не может быть отрицательной.")
        elif not isinstance(self.salary, (int, float, str)):
            raise ValueError("Зарплата должна быть числом или строкой 'Зарплата не указана'.")

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


if __name__ == "__main__":
    vacancy1 = Vacancies("водитель", 80000, "водитель-дальнобойщик", "ссылка")
    vacancy2 = Vacancies("механик", 90000, "механик-универсал", "ссылка1")
    print(vacancy1)
    print(vacancy2 > vacancy1)