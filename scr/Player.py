from scr.TeamMember import TeamMember


class Player(TeamMember):
    def __init__(self, name, skills, aim):
        super().__init__(name, "Гравець")
        self.skills = skills
        self.aim = aim  # Базова характеристика aim (точність)

    def calculate_performance(self, morale):
        """Обчислює продуктивність залежно від моралі команди."""
        performance_multiplier = 1 + (morale - 5) * 0.1  # Чим вище мораль, тим більший множник
        return round(self.aim * performance_multiplier, 2)

    def get_details(self):
        return f"{self.role}: {self.name}, Навички: {', '.join(self.skills)}, Aim: {self.aim}"
