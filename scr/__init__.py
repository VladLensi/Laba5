# from team_member import Player, Coach, Staff
# from team import Team
# from tournament import Tournament
# from sponsor import Sponsor
# from training_program import TrainingProgram

my_team = Team("Cyber Titans")
player1 = Player("Alex", ["Sniping", "Strategy"])
coach = Coach("Chris", "Aggressive Style")
analyst = Staff("Taylor", "Analyst")

my_team.recruit_member(player1)
my_team.recruit_member(coach)
my_team.recruit_member(analyst)

# турнір
tournament = Tournament("World Cup", 100000)
print(tournament.participate(my_team))

# тренування
training = TrainingProgram("Bootcamp", 7)
print(training.organize_practice(my_team))

# cпонсорство
sponsor = Sponsor("Tech Corp", ["High performance", "Fanbase"])
print(sponsor.negotiate(my_team))

# аналіз
print(my_team.analyze_performance())

# деталі команди
for detail in my_team.get_team_details():
    print(detail)
