from abc import ABC, abstractmethod

# Абстрактний базовий клас TeamMember
class TeamMember(ABC):
    def __init__(self, name, role):
        self.name = name
        self.role = role

    @abstractmethod
    def get_details(self):
        """Абстрактний метод для отримання деталей про члена команди"""
        pass

    @abstractmethod
    def calculate_performance(self, morale):
        """Абстрактний метод для розрахунку продуктивності члена команди"""
        pass


# Підклас Player (гравець)
class Player(TeamMember):
    def __init__(self, name, skills, aim):
        super().__init__(name, "Гравець")
        self.skills = skills  # Навички гравця
        self.aim = aim  # Точність гравця (значення від 0 до 100)

    def get_details(self):
        return f"{self.role}: {self.name}, Навички: {', '.join(self.skills)}, Точність: {self.aim}%"

    def calculate_performance(self, morale):
        """Розрахунок продуктивності гравця залежно від його точності та моралі."""
        base_performance = sum(len(skill) for skill in self.skills)  # Продуктивність базується на кількості навичок
        adjusted_performance = base_performance * (self.aim / 100) * (1 + morale / 10)
        return round(adjusted_performance, 2)


# Підклас Coach (тренер)
class Coach(TeamMember):
    def __init__(self, name, specialization, strategy_bonus):
        super().__init__(name, "Тренер")
        self.specialization = specialization  # Стиль тренера
        self.strategy_bonus = strategy_bonus  # Бонус до стратегії (від 1.0 до 2.0)

    def get_details(self):
        return f"{self.role}: {self.name}, Спеціалізація: {self.specialization}, Бонус стратегії: {self.strategy_bonus}"

    def calculate_performance(self, morale):
        """Тренери впливають на загальний бонус до продуктивності."""
        return morale * self.strategy_bonus


# Підклас Staff (персонал)
class Staff(TeamMember):
    def __init__(self, name, position, efficiency):
        super().__init__(name, "Персонал")
        self.position = position  # Посада (аналітик, психолог тощо)
        self.efficiency = efficiency  # Ефективність роботи (від 0.5 до 1.5)

    def get_details(self):
        return f"{self.role}: {self.name}, Посада: {self.position}, Ефективність: {self.efficiency}"

    def calculate_performance(self, morale):
        """Персонал покращує мораль команди."""
        return morale * self.efficiency
