from ast import main
from TeamMember import Player, Coach, Staff
from Team import team
# from tournament import Tournament
from Sponsor import sponsor
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
     
    print("")
    print("1. Вивести список спорцменів.")
    print("2. Створити команду.")
    print("3. Пошук спонсорів.")
    print("4. Перевірити баланс ($).")
    print("5. Тренувати учасника команди. Вартість 2000$")
    print("6. Організувати тренувальний процес. Вартість 10000$")
    print("7. Організувати підготовку до турніру. Вартість 8000$ (підвищує дух команди в турнірі).")#дух команди +1 для участі в турнірах
    print("8. Зколаборуватися з брендами; створити мерч. Вартість 20000$.")#є шанс окупити і навпаки
    print("9. Організувати зустріч з фанатами.")#у вас не буде фанатів якщо багато програєте в турнірах, фани впливають на мерч і мораль
    print("10. Прийняти участь в турнірі.")#заробити багато грошей або ні. Здобути славу або ні і тд.
    print("0. Вийти з програми.")

def main():

    print("Вітаємо в симуляції менеджера кіберспортивної команди!\n\n")

    tryes = 0

    money = 10000
    morality = 10

    while True:
        
        PrintMenu()

        userInput = input("\nОберіть опцію:")#\n для читабельності зробив

        if userInput == '1':
            print("\nTут буде функціонал.")

        elif userInput == '2':
            print("\nTут буде функціонал.")

        elif userInput == '3':
            print("\nTут буде функціонал.")

        elif userInput == '4':
            print(f"\nВаш баланс: {money}$.")
            
        elif userInput == '0':
            print("\nДякую за використання програми!.")
            print("Виконується вихід...")
            break

        else:
            print("Ми ж з вами серйозні люди? Введіть чифрове значення від 0 до 10.")
            tryes + 1
            if tryes > 3:
                print("\nАх ти... Тримай маслину! -1000$")
                print("Будеш знати!")
                money - 1000
                tryes = 4
                print(f"\nВаш баланс: {money}$.")

if __name__ == "__main__":
    main()