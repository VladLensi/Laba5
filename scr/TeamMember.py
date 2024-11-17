from abc import ABC, abstractmethod

# Абстрактний базовий клас TeamMember
class TeamMember(ABC):
    def __init__(self, name, role):
        self.name = name
        self.role = role

    @abstractmethod
    def get_details(self):
        """Метод для отримання деталей про члена команди"""
        pass


# Підклас Player (гравець)
class Player(TeamMember):
    def __init__(self, name, skills):
        super().__init__(name, "Гравець")
        self.skills = skills

    def get_details(self):
        """Реалізував мето для отримання деталей про гравця"""
        return f"{self.role}: {self.name}, Навички: {', '.join(self.skills)}"


# Підклас Coach (тренер)
class Coach(TeamMember):
    def __init__(self, name, specialization):
        super().__init__(name, "Тренер")
        self.specialization = specialization

    def get_details(self):
        """Метод для отримання деталей про тренера"""
        return f"{self.role}: {self.name}, Спеціалізація: {self.specialization}"


# Підклас Staff (персонал)
class Staff(TeamMember):
    def __init__(self, name, position):
        super().__init__(name, "Персонал")
        self.position = position

    def get_details(self):
        """Метод для отримання деталей про персонал"""
        return f"{self.role}: {self.name}, Посада: {self.position}"
