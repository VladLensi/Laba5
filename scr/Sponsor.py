class Sponsor:
    def __init__(self, name, requirements):
        self.name = name
        self.requirements = requirements

    def negotiate(self, team):
        return f"Negotiating sponsorship for team {team.name} with {self.name}."
