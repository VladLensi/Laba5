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

def PrintMenu():
    print("Оберіть опцію:")
    print("1. Вивести список спорцменів.")
    print("2. Створити команду.")
    print("3. Пошук спонсорів.")
    print("4. Організувати тренувальний процес (коштує 1000$).")
    print("5. Організувати підготовку до турніру (коштує 500$ та підвищує дух команди в турнірі).")#дух команди +1 для участі в турнірах
    print("6. Зколаборуватися з брендами; створити мерч (коштує 2000$).")#є шанс окупити і навпаки
    print("7. Організувати зустріч з фанатами.")#у вас не буде фанатів якщо багато програєте в турнірах
    print("8. Прийняти участь в турнірі.")#заробити багато грошей або ні. Здобути славу або ні і тд.




#while (True):

