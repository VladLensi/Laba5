class Team:
    def __init__(self, name):
        self.name = name
        self.members = []

    def recruit_member(self, member):
        self.members.append(member)

    def analyze_performance(self):
        # Логіка аналізу (можна доповнити)
        return f"Analyzing performance of {self.name}."

    def get_team_details(self):
        return [member.get_details() for member in self.members]
