# from scr import Player
#from scr.TeamMember import TeamMember


class team:
    def __init__(self, name):
        self.name = name
        self.members = []  # Список членів команди
        self.budget = 10000  # Початковий бюджет
        self.morale = 5  # Початковий рівень моралі (1-10)

    def recruit_member(self, member):
        """Додає нового члена команди."""
        if isinstance(member, TeamMember):
            self.members.append(member)
            print(f"{member.name} додано до команди {self.name}.")
        else:
            print("Член має бути об'єктом класу TeamMember.")

    def analyze_performance(self):
        """Аналіз виступів команди."""
        total_performance = 0
        for member in self.members:
            if isinstance(member, Player):
                performance = member.calculate_performance(self.morale)
                print(f"Гравець {member.name} з aim {member.aim} має продуктивність: {performance}")
                total_performance += performance
        return f"Загальна продуктивність команди: {total_performance}"

    def get_team_details(self):
        """Повертає деталі про всіх членів команди."""
        return [member.get_details() for member in self.members]

    def update_budget(self, amount):
        """Оновлює бюджет команди."""
        self.budget += amount
        print(f"Бюджет оновлено. Новий бюджет: {self.budget}$.")

    def update_morale(self, change):
        """Оновлює мораль команди."""
        self.morale = max(1, min(10, self.morale + change))
        print(f"Мораль команди оновлено. Поточна мораль: {self.morale}.")
