import random

from scr import Player


class Tournament:
    def __init__(self, name, prize_pool, difficulty):
        self.name = name
        self.prize_pool = prize_pool
        self.difficulty = difficulty  # Складність турніру (1-10)

    def participate(self, team):
        """Участь у турнірі залежно від продуктивності команди."""
        print(f"Команда {team.name} бере участь у турнірі {self.name}.")
        total_performance = 0

        # Розрахунок загальної продуктивності команди
        for member in team.members:
            if isinstance(member, Player):
                performance = member.calculate_performance(team.morale)
                total_performance += performance

        # Шанси на перемогу
        success_chance = total_performance / (self.difficulty * 100)
        print(f"Загальна продуктивність команди: {total_performance}")
        print(f"Шанси на перемогу: {round(success_chance * 100, 2)}%")

        # Визначення результату
        if random.random() < success_chance:
            team.update_budget(self.prize_pool)  # Додати виграш до бюджету
            team.update_morale(2)  # Підвищити мораль
            return f"Команда {team.name} перемогла в турнірі {self.name}! Призовий фонд: {self.prize_pool}$"
        else:
            team.update_morale(-2)  # Знизити мораль у разі програшу
            return f"Команда {team.name} програла в турнірі {self.name}. Спробуйте ще раз."
