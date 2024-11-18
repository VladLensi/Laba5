from ast import main
from TeamMember import Player, Coach, Staff
from Team import team
# from tournament import Tournament
# from sponsor import Sponsor
# from training_program import TrainingProgram

my_team = team("Cyber Titans")
player1 = Player("Alex", ["Sniping", "Strategy"])
coach = Coach("Chris", "Aggressive Style")
analyst = Staff("Taylor", "Analyst")

my_team.recruit_member(player1)
my_team.recruit_member(coach)
my_team.recruit_member(analyst)

# турнір
# tournament = Tournament("World Cup", 100000)
# print(tournament.participate(my_team))

# # тренування
# training = TrainingProgram("Bootcamp", 7)
# print(training.organize_practice(my_team))

# # cпонсорство
# sponsor = Sponsor("Tech Corp", ["High performance", "Fanbase"])
# print(sponsor.negotiate(my_team))

# аналіз
print(my_team.analyze_performance())

# деталі команди
for detail in my_team.get_team_details():
    print(detail)

def PrintMenu():

    print("1. Вивести список спорцменів.")
    print("2. Створити команду.")
    print("3. Пошук спонсорів.")
    print("4. Тренувати учасника команди. Вартість 1000$")
    print("5. Організувати тренувальний процес. Вартість 1000$")
    print("6. Організувати підготовку до турніру. Вартість 500$ (підвищує дух команди в турнірі).")#дух команди +1 для участі в турнірах
    print("7. Зколаборуватися з брендами; створити мерч. Вартість 2000$.")#є шанс окупити і навпаки
    print("8. Організувати зустріч з фанатами.")#у вас не буде фанатів якщо багато програєте в турнірах
    print("9. Прийняти участь в турнірі.")#заробити багато грошей або ні. Здобути славу або ні і тд.
    print("0. Вийти з програми.")

def main():
    while True:
        
        PrintMenu()

        userInput = input("Оберіть опцію:")

        if userInput == '1':
            print("Tут буде функціонал.")

        if userInput == '2':
            print("Tут буде функціонал.")

        if userInput == '3':
            print("Tут буде функціонал.")
            
        if userInput == '0':
            print("Дякую за використання програми!.")
            print("Виконується вихід...")
        break

if __name__ == "__main__":
    main()