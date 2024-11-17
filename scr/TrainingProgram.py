class TrainingProgram:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

    def organize_practice(self, team):
        return f"Organizing {self.name} for team {team.name} for {self.duration} days."
