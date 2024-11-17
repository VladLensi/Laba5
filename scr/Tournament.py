class Tournament:
    def __init__(self, name, prize_pool):
        self.name = name
        self.prize_pool = prize_pool

    def participate(self, team):
        return f"Team {team.name} is participating in {self.name}!"
