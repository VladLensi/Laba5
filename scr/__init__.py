from ast import main
from TeamMember import Player, Coach, Staff
from Team import team
# from tournament import Tournament
from Sponsor import sponsors
# from training_program import TrainingProgram
    
    # СТРУКТУРА ДЛЯ ПОШУКУ
    # for emp in employees:
    #     if (emp['surname']) == newAppointment:
    #         app = input (str("Input new appointment: "))
    #         emp['appointment'] = str(app)
    #         print(f"New appointment: {app} of {emp['name']} {emp['surname']}")
    #     else: 
    #         print(f"Employee with surname {newAppointment} did not found.")

# my_team = team("Cyber Titans")
# player1 = Player("Alex", ["Sniping", "Strategy"])
# coach = Coach("Chris", "Aggressive Style")
# analyst = Staff("Taylor", "Analyst")

# my_team.recruit_member(player1)
# my_team.recruit_member(coach)
# my_team.recruit_member(analyst)

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
# print(my_team.analyze_performance())

# #деталі команди
# for detail in my_team.get_team_details:
#     print(detail)

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
    print("10. Прийняти участь в турнірі. Початкови вклад 30000$")#заробити багато грошей або ні. Здобути славу або ні і тд.
    print("0. Вийти з програми.")

def main():
    print("Вітаємо в симуляції менеджера кіберспортивної команди!")

    merchAbility = False
    tries = 0
    money = 10000
    morality = 10
    moneyMultiply = 1
    fans = 10
    sponsorIsChoosen = False


    while True:

        PrintMenu()

        userInput = input("\nОберіть опцію: ")  # \n для читабельності зробив везде

        if userInput == '1':
            print("\nTут буде функціонал.")

        elif userInput == '2':
            print("\nTут буде функціонал.")

        elif userInput == '3':
            if sponsorIsChoosen:
                print("Ви вже підписали контракт зі спонсором.")
                continue

            print("\nДоступні спонсори:")
            for index, sponsor in enumerate(sponsors, start=1):
                print(f"{index}. {sponsor}")
            
            print("0. Відмовитися від вибору та повернутися до головного меню.")

            # вибір спонсора
            while True:
                try:
                    choice = int(input("\nВиберіть номер спонсора або введіть 0 для повернення: "))
                    
                    if choice == 0:
                        print("Відмова від вибору. Повертаємося до головного меню.")
                        break

                    elif 1 <= choice <= len(sponsors):
                        selectedSponsor = sponsors[choice - 1]
                        
                        if money < selectedSponsor.price:
                            print("\nУ вас недостатньо коштів.")
                            break
                        else:
                            print(f"\nВи обрали спонсора: {selectedSponsor.name}")

                            # оновлення даних
                            money += selectedSponsor.price
                            moneyMultiply = selectedSponsor.moneyMultiply
                            fans += selectedSponsor.fans
                            merchAbility = selectedSponsor.GETmerchAbility()

                            sponsorIsChoosen = True

                            print(f"Ви отримали {selectedSponsor.price}$, множник виграшу x{moneyMultiply}, фанати: +{selectedSponsor.fans}.")
                            print(f"Можливість створення мерчу: {'Так' if merchAbility else 'Ні'}")
                            break

                    else:
                        print("Неправильний номер. Введіть число від 1 до", len(sponsors))

                except ValueError:
                    print("Введіть числове значення.")


        elif userInput == '4':
            print(f"\nВаш баланс: {money}$.")

        elif userInput == '5':
            #print players але не всіх тільки тих хто в команді(мб створити новий файл під них)
            PlayerChoise = input("Введіть і'мя члена команди: ")
            money -= 2000
 
        elif userInput == '10':
            print("Тут буде важко.")
            #sponsorIsChoosen == False

        elif userInput == '0':
            print("\nДякую за використання програми!.")
            print("Виконується вихід...")
            break

        else:
            print("Вибрана неправильна опція, спробуйте ще раз.")
            tries += 1
            if tries > 3:
                print("\nАх ти... Тримай маслину! -1000$")
                print("Будеш знати!")
                money -= 1000  # Виправлено
                tries = 4
                print(f"\nВаш баланс: {money}$.")

if __name__ == "__main__":
    main()